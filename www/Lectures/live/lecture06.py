def cast_of_chars(txt: str) -> set:
  '''Given a string of text, find all the words that begin with 
  a capital letter. Return a set (no duplicates) containing those 
  words, converted to all-caps. 
  '''
  # split txt into words by blank space 
  words = txt.split()
  
  # throw away words that don't start with capitals
  caps_words: set[str] = set()
  for word in words:
      if word[0].isupper():
        caps_words.add(word)

  # get rid of punctuation 
  cleaned_words: set[str] = set()
  for word in caps_words: 
     cleaned_words.add(word.replace(',', '').replace('.', '').replace('!', ''))

  # all-caps the remaining words 
  all_caps = set()
  for word in cleaned_words: 
     all_caps.add(word.upper())
  return all_caps



# Let's write some examples first. Do we understand the problem? 

assert cast_of_chars('hello world i have no capital letters') == set()
assert cast_of_chars('Hello Hello goodbye') == {'HELLO'} 
assert cast_of_chars('Hi! This is a sentence.') == {'THIS', 'HI'}

print(cast_of_chars('hello world i have no capital letters'))
print(cast_of_chars('Hello Hello goodbye'))
print(cast_of_chars('Hi! This is a sentence.'))

#

input = [-4, 5, 6, -1, 0, 2]
[i for i in input if i > 0]
{i for i in input if i > 0}











# ###############################################################
# # Not everything we need, but useful pieces. Put them in order,
# #   but keep in mind there may be "holes" -- don't worry about 
# #   that yet. Note where something is missing with a ??? comment.

# # caps_words.add(word)
# # cleaned.add(word) 
# # for word in cleaned:
# # words = s.split() 
# # for word in caps_words: 
# # for word in words:         
# # all_caps.add(word) 





# ##########################
# # Comprehensions: other examples
# ##########################


# # Example input data
# courses_taken = {'tim': 5, 'nim': 17, 'annabelle': 18}

# # get list of names (capitalized) 
# # who have upper-class status (16+ courses taken)
# uc_1 = []
# for name in courses_taken: 
#     if courses_taken[name] >= 16:
#         uc_1.append(name.upper())
# print(uc_1)

# # same thing, but with "list comprehension"
# #  [<expression> for <id> in <list/set> if <condition>]
# # The "if" part is optional.
# uc_2 = [name.upper() for name in courses_taken if courses_taken[name] >= 16]
# print(uc_2)

# # This also works for ranges. E.g., to get 0,1,2,0,1,2,... for 100 elements:
# print([num % 3 for num in range(100)])









# # Comprehensions work for sets as well. 
even_numbers_to_100 = {num for num in range(101) if num % 2 == 0}
# # {0, 2, 4, 6, ...}
print(even_numbers_to_100)



# # "if" works for list comprehension too.
# odd_numbers_to_100_ordered = [num for num in range(101) if num % 2 == 1] 
# print(odd_numbers_to_100_ordered)


# # Dictionary comprehensions. The expression is a key:value pair
successors_to_numbers_to_100 = {num : num+1 for num in range(101) if num % 3 == 0 and num > 50}
print(successors_to_numbers_to_100)

# [ADD_THIS(THING) for THING in COLLECTION if CONDITION]

# ######################
# # cast_of_characters with comprehensions
# ######################

# # Which do you prefer? I tend to like comprehensions when I can easily use them,
# # and when they produce something that's easier to follow. Once you know the syntax,
# # this is likely to be more readable. But at the moment, for loops may be quicker to read.
def cast_of_chars_with_comprehensions(s: str):      
    words = s.split() 
    caps_words = {word for word in words if word.isupper()} 
    cleaned = {word.replace(",", "") for word in caps_words}
    all_caps = {word.upper() for word in cleaned}
    return all_caps
