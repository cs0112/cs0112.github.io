# In-class code from Dec 4, 2024

# This gives us actual wall-clock time elapsed via the most fine-grained clock available
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
# 10 options for each digit, 10 digits, 10,000,000,000

def can_login(tried_password: str) -> bool: 
    #return password == tried_password
    # Let's manually implement string equality:
    if len(tried_password) != len(password): return False 
    idx = 0 
    while idx < len(password): 
        if password[idx] != tried_password[idx]:
            return False
        idx += 1
    return True

def attack(trials: int):
    times: dict[str, list[int]] = {}
    for i in range(0, trials):
        for first_char in options: 
            start = perf_counter_ns()
            probe_guess = first_char + ''.join(random.choices(options, k=password_length-1))
            # NOTE: This is what I missed in class. I forgot to change this from `first_char`
            # to `probe_guess`, so we weren't benefitting from the random suffix at all. 
            can_login(probe_guess)
            end = perf_counter_ns()
            if first_char not in times: times[first_char] = []
            times[first_char].append(end-start)
    aggregated = {k:min(times[k]) for k in times}
    print(aggregated)

if __name__ == '__main__':
    attack(5)





# 


# sorted(result, key = lambda c : counts[c], reverse=True)