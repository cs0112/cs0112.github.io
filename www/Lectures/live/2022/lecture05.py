print('Hi!')

# set(...)
# list(...)

ingredients = ['flour', 'salt', 'flour', 'sugar']
print(ingredients)  
print(set(ingredients)) # what would you like here?
print(list(set(ingredients))) # what would you like here?

# list(set: list with no duplicates?
# set(: the ingredients without duplicates? and maybe no order

more_ingredients = list(ingredients)
more_ingredients.append('cinnamon')
print(ingredients)  
print(more_ingredients)

recipes = {'pbj': {'peanut butter', 'jelly', 'bread'},
           'smoothie': {'peanut butter', 'banana', 'oat milk'}}
#chocolate_smoothie = set(recipes['smoothie'])
chocolate_smoothie = recipes['smoothie']
chocolate_smoothie.add('cocoa powder')
berry_smoothie = recipes['smoothie'] | {'berries'}

print(recipes)
print(chocolate_smoothie)
print(berry_smoothie)

# set() # empty set
example = dict()
empty_list = list() # []

list1 = [2]
list2 = [3]
list1.append(12)
print(list1)
print(list2)

list1 = [2]
list2 = [2]
list3 = list(list2)
print(list1 == list2) # What should this return?
print(id(list1))
print(id(list2))
print(id(list3))


def add_len_to_list(l: list):
    l.append(len(l))    

def test_add_len_to_list_twice():
    list_local = []         # setup
    add_len_to_list(list_local)
    assert list_local == [0]
    add_len_to_list(list_local)
    assert list_local == [0,1]
test_add_len_to_list_twice()











