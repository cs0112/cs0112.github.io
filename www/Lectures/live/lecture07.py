
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


