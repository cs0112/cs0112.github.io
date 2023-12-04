##########################
# From last time, here is cast_of_chars
# I like to:
# (1) start building a function outside-in, leaving holes where 
#   I'm not yet sure what to do.
# (2) give names to intermediate values, rather than trying to 
#   put everything together at once (which can be overwhelming
#   to read, even for me)
# (3) for functions like this, I like to use *comprehensions*, 
#   which I demo below. 
##########################

def cast_of_chars(s: str):      
    words = s.split() # split by blank space
    caps_words = set() 
    for word in words: 
        if word[0].isupper(): # check first letter
            caps_words.add(word)
    cleaned = set()
    for word in caps_words: 
        cleaned.add(word.replace(",", "")) # remove commas
    all_caps = set()
    for word in cleaned:
        all_caps.add(word.upper()) # fully uppercase
    return all_caps







# Which do you prefer? I tend to like this when I can easily use 
# comprehensions, because it feels more "declarative"; fewer 
# chances for *me* to make a mistake in how the for-loop goes.
def cast_of_chars_with_comprehensions(s: str):      
    words = s.split() 
    caps_words = {word for word in words if word.isupper()} 
    cleaned = {word.replace(",", "") for word in caps_words}
    all_caps = {word.upper() for word in cleaned}
    return all_caps




##########################
# Comprehensions: smaller examples
##########################


# Example input data
courses_taken = {'tim': 5, 'nim': 17, 'annabelle': 18}

# get list of names (capitalized) 
# who have upper-class status (16+ courses taken)
uc_1 = []
for name in courses_taken: 
    if courses_taken[name] >= 16:
        uc_1.append(name.upper())
print(uc_1)

# same thing, but with "list comprehension"
#  [<expression> for <id> in <list/set> if <condition>]
# The "if" part is optional.
uc_2 = [name.upper() for name in courses_taken if courses_taken[name] >= 16]
print(uc_2)

# This also works for ranges. E.g., to get 0,1,2,0,1,2,... for 100 elements:
print([num % 3 for num in range(100)])









# Comprehensions work for sets as well. 
even_numbers_to_100 = {num for num in range(101) if num % 2 == 0}
# {0, 2, 4, 6, ...}
print(even_numbers_to_100)



# "if" works for list comprehension too.
odd_numbers_to_100_ordered = [num for num in range(101) if num % 2 == 1] 
print(odd_numbers_to_100_ordered)







# Dictionary comprehensions. The expression is a key:value pair
successors_to_numbers_to_100 = {num : num+1 for num in range(100)}
print(successors_to_numbers_to_100)




##########################
# Machine Learning
##########################


# example classifier: is this a dog, or a cat?
def dog_or_cat(size: int, fuzziness: int):
    if size > 10: 
        return 'dog'
    if size > 8 and fuzziness > 10: 
        return 'dog'
    else:
        return 'cat'
















song1 = """
And here I go again, I'm drinkin' one, I'm drinkin' two
I got my heartache medication, a strong dedication
To gettin' over you, turnin' me loose
On that hardwood jukebox lost in neon time...
"""






song2 = """
Happy Birthday to You
Happy Birthday to You
Happy Birthday Dear Bruno
Happy Birthday to You.
"""
# How many times does each word occur?
term_frequency = {
    'Happy': 4,
    'Birthday': 4,
    'to': 3,
    'Dear': 1,
    'Bruno': 1,
    'You': 3
}

# Example of how the above word-counts might be adjusted based on 
# how common the words are in general
tf_with_idf = {
    'Happy': 4,
    'Birthday': 8,
    'to': 0,
    'Dear': 2,
    'Bruno': 8,
    'You': 1.5
}


