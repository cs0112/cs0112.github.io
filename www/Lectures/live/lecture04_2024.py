
dry_ingredients = ['flour', 'baking powder']
dry_ingredients = dry_ingredients + ['cinnamon']

recipes = {'pbj': {'pb', 'jelly', 'bread'},
           'smoothie': {'pb', 'banana', 'milk'}}

chocolate_smoothie = recipes['smoothie']
chocolate_smoothie.add('chocolate')
print(recipes['smoothie'])
vanilla_smoothie = recipes['smoothie']
vanilla_smoothie.add('vanilla')