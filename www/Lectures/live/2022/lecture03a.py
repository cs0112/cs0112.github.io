print('Happy Monday!')

# Lists
story = ['It', 'was', 'a', 'dark', 'and']
story.append('stormy') # *changes the list*
print(story)
print(story[0]) # indexes start with zero
# print(story[17]) # IndexError
print(story + ['night.'])
print(story)
for word in story:
    print(word)

# Dictionaries
status = {
    'brightness': 'dark', 
    'weather': 'stormy'
}
print(status['weather'])
# print(status['not there']) # KeyError
# print(status['stormy']) # KeyError
print('weather' in status)
status['day'] = 'monday' # MODIFIED
print(status)
# Sets
night = {'dark', 'stormy'}
print(night)
night.add('frightening') # MODIFIED
print(night)
for element in night:
    print(element)
# without modifying:
print(night | {'inauspicious'})
print(night)    