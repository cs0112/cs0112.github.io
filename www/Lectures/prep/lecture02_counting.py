def count_words(s: str) -> dict:
    counts = {}
    for word in s.split():
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts

def most_common(counts: dict):
    most_common = ''
    most_common_count = 0
    for word in counts:   
        if counts[word] > most_common_count:
            most_common = word
            most_common_count = counts[word]
    return most_common

# if __name__ == '__main__':
#     import sys
#     print(most_common(count_words(open(sys.argv[1], 'r').read())))


# This fails!
# assert count_words("Why do I feel bitter when I should be feeling sweet?") == {
#     "Why": 1, "do": 1, "I": 2, "feel": 1, "bitter": 1, "when": 1, 
#     "should": 1, "be": 1, "feeling": 1, "sweet": 1}    
# why? 
# print(count_words("Why do I feel bitter when I should be feeling sweet?"))
# Because of the *question mark*
assert count_words("Why do I feel bitter when I should be feeling sweet?") == {
    "Why": 1, "do": 1, "I": 2, "feel": 1, "bitter": 1, "when": 1, 
    "should": 1, "be": 1, "feeling": 1, "sweet?": 1}    