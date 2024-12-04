# This module contains a toy demo of a timing attack executed on a login system. 
# We'll do a basic version of this in livecode, but this is my prep.

# actual wall-clock time elapsed, most fine-grained clock available
from time import perf_counter_ns 
import random
import string

# Assumption: we know in advance how long the password is. This isn't realistic, 
# but we can make a more sophisticated version that works for multiple lengths.
password_length: int = 10
# Assumption: characters are always digits (0 through 9). This is also not realistic, 
# but we could expand the character set. 
options = string.digits

# Hard-coded password target
password = '1234567890'

def string_equal(s1: str, s2: str) -> bool: 
    '''Write our own string equality function to amplify the signal and demo what's going on. 
       Python has a faster, native implementation that is harder to do a quick demo with. :-)
       Even so, this sort of attack has been used against real systems!'''
    if len(s1) != len(s2): return False 
    idx = 0
    while idx < len(s1):
        if s1[idx] != s2[idx]: return False
        idx = idx + 1
    return True

# Note: I believe that the reason Python's default string == won't allow for this attack
# has to do with how its implementation compares blocks of memory. Strings, like lists 
# in Python, are stored in contiguous blocks of memory. So I believe what's happening there
# is the comparison isn't character-by-character, but in larger chunks: perhaps 64 bits at 
# a time, or something like that. Thus, an early mismatch could be because of the 2nd 
# character as much as because of the 1st! I want to test this out, but I should upload 
# this code for now. :-)

def can_login(entered: str) -> bool:
    '''We could just call string_equal in this demo, but I like having this 
    seemingly pointless helper to indicate the attacker doesn't have the password,
    but can call some login function.'''
    return string_equal(entered, password)

def keys_by_likelyhood(counts: dict[str, int]) -> list[str]: 
    '''Helper to return a highest-value key in the given dictionary. 
    If there is a tie, return the first such key.'''
    result = list(counts.keys()) # unsorted list to start with
    return sorted(result, key = lambda c : counts[c], reverse=True)

def attack(trials: int, best_prefix: str, remaining_length: int) -> tuple[bool, int, int]:
    '''Run the attack, using <trials> attempts per character. When calling this 
    function externally, pass the empty string for <best_prefix>, and the password 
    length for <remaining_length>. 
    Returns whether the correct password was found, and how many actual guesses were made.'''
    
    # If we've hit the target length, don't keep attacking. Make a guess. 
    if remaining_length < 1: 
        is_correct = can_login(best_prefix)
        print(f'I guess that the password is: {best_prefix}. Guess is: {is_correct}')
        return (is_correct, 0, 1) # count this "real" guess, no probes

    count_probe_guesses = 0
    count_real_guesses = 0
    times: dict[str, list[int]] = dict()
    for i in range(0, trials):
        for c in options: 
            # Start with <c>, end randomly
            probing_guess: str = best_prefix + c + ''.join(random.choices(options, k=remaining_length-1))
            
            start = perf_counter_ns()
            can_login(probing_guess)
            end = perf_counter_ns()
            count_probe_guesses += 1 # count this probing guess
            
            if c not in times: times[c] = []
            times[c].append((end - start))

    # Use minimum to amplify signal by removing extra computation being done on SOME, but not ALL
    # trials. Surely the right guess won't have a small min?
    aggregated: dict[str, int] = {k: min(times[k]) for k in times.keys()}
    # print(f'Remaining {remaining_length}, aggregated: {aggregated}')
    
    # Try characters in order of our confidence in their correctness
    try_in_order = keys_by_likelyhood(aggregated)
    
    for best_character in try_in_order: 
        was_correct,probe_guesses_made,real_guesses_made = attack(trials, best_prefix+best_character, remaining_length-1)
        count_probe_guesses += probe_guesses_made
        count_real_guesses += real_guesses_made
        # If we found the real password, we don't need to do any more work. 
        if was_correct: return (True, count_probe_guesses, count_real_guesses)
    # None of our exploration for this current guess succeeded. :-(
    return (False, count_probe_guesses, count_real_guesses)

# EXERCISE: experiment with the number of trials per character! 
# 1 is too small: we can't reduce noise at all. 5 works well on my laptop.
if __name__ == '__main__':
    print('--------------------------------------------------------------')
    print(f'There are {pow(len(options), password_length):_} possible password strings of length {password_length}, using characters {options}.')
    found, probe_count, real_count = attack(5, '', password_length)
    print(f'Found = {found} using {probe_count} probes and {real_count} real guesses.')
    print()