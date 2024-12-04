# dry_ingredients = ['flour', 'baking powder']
# dry_ingredients = dry_ingredients + ['cinnamon']
# print(dry_ingredients)

recipes = {'pbj': {'peanut butter', 'jelly', 'bread'},
           'smoothie': {'peanut butter', 'banana', 'oat milk'}}
chocolate_smoothie = recipes['smoothie']
chocolate_smoothie.add('cocoa powder')
berry_smoothie = recipes['smoothie'] | {'berries'}

print(recipes)
print(chocolate_smoothie)
print(berry_smoothie)




# NOTE(sep14) Python adds a lot of "convenience" features, especially for printing. 
# Here's one that I like to use often. You don't have to use this if you
# don't want to! You might find it convenient, though. 
# You could just print(recipes) etc. and it would work fine. But I like using 
#   Python's "format strings", which let you put expressions from the program
#   inside braces, which are then automatically inserted into the string. This
#   way, you can easily add labels, etc.
# print(f'recipes={recipes}')
# print(f'chocolate_smoothie={chocolate_smoothie}')
# print(f'berry_smoothie={berry_smoothie}')

