def memory_demo():
    recipes = {'pbj': {'peanut butter', 'jelly', 'bread'},
               'smoothie': {'peanut butter', 'banana', 'oat milk'}}
    # chocolate_smoothie = recipes['smoothie']
    chocolate_smoothie = set(recipes['smoothie'])
    chocolate_smoothie.add('cocoa powder')    
    print(recipes)
    print(chocolate_smoothie)
    # ? How are these objects all related in memory? Let's draw a picture.

    # what if we did this instead?
    # chocolate_smoothie = list(recipes['smoothie'])
    #chocolate_smoothie.add('cocoa powder')


# Used for the 2nd part of today's class
def add_len_to_list(lst: list):
    lst.append(len(lst))


# Note what happens in the _test_ file if we don't include this if statement
if __name__ == '__main__':
    memory_demo()
