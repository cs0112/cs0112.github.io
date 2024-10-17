

courses_taken = {'tim': 5, 'nim': 17, 'annabelle': 18}
# get list of students who have upper-class status (16+)
uc = []
for name in courses_taken: 
    if courses_taken[name] >= 16:
        uc.append(name)
print(uc)
# "list comprehension"
# capitalize
uc_2 = [name.upper() for name in courses_taken if courses_taken[name] > 16]
print(uc_2)
print([num % 3 for num in range(100)])












# ## Comprehensions
# #  set example with useful syntax
# even_numbers_to_100 = {num for num in range(101) if num % 2 == 0}
# # {0, 2, 4, 6, ...}
# print(even_numbers_to_100)










# # list comp. example
# odd_numbers_to_100_ordered = [num for num in range(101) if num % 2 == 1] 
# print(odd_numbers_to_100_ordered)

# # dictionary comp. example
# successors_to_numbers_to_100 = {num : num+1 for num in range(100)} # ???
# print(successors_to_numbers_to_100)














# ######

# # example classifier
# def dog_or_cat(size: int, fuzziness: int):
#     if size > 10: 
#         return 'dog'
#     if size > 8 and fuzziness > 10: 
#         return 'dog'
#     else:
#         return 'cat'

# ######

















# song1 = """
# And here I go again, I'm drinkin' one, I'm drinkin' two
# I got my heartache medication, a strong dedication
# To gettin' over you, turnin' me loose
# On that hardwood jukebox lost in neon time...
# """





# ######

# song2 = """
# Happy Birthday to You
# Happy Birthday to You
# Happy Birthday Dear Bruno
# Happy Birthday to You.
# """
# # How many times does each word occur?
# term_frequency = {
#     'Happy': 4,
#     'Birthday': 4,
#     'to': 3,
#     'Dear': 1,
#     'Bruno': 1,
#     'You': 3
# }

# # Example of how these might be adjusted based on 
# # how common the words are in general
# tf_with_idf = {
#     'Happy': 4,
#     'Birthday': 8,
#     'to': 0,
#     'Dear': 2,
#     'Bruno': 8,
#     'You': 1.5
# }


