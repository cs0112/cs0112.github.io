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
    # memory_demo()
    input = []
    result = add_len_to_list(input)  # [0]
    # assert result == [0] # NO 
    assert input == [0]
    print(f'example={1+1}')
    print(f'result={result}')
    print(f'input={input}')
    add_len_to_list(input)
    assert input == [0, 1]
    add_len_to_list(input)
    assert input == [0, 1, 2]
    add_len_to_list(input)
    add_len_to_list(input)
    print(f'input={input}')
    
    print(f'[0,1]==(0,1) : {[0,1]==(0,1)}')
    print(f'[0,1]==[0,1] : {[0,1]==[0,1]}')
    print(f'[0,1] is [0,1] : {[0,1] is [0,1]}')
    print(f'id: {id([0,1])}')
    print(f'id: {id([0,1])}')

# (1) set up: create inputs, context objects, etc. 
# (2) run the code under test 
# (3) check the result (including context!)
# (4) clean up 

