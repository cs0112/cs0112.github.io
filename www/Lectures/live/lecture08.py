
# How many "basic operations" in the worst and best case?
# (Remember "best" and "worst" are not about input size. Rather, they're about how 
#  two inputs of the same size might have different performance in the program.)
def count_the(l: list) -> int:
    count = 0            
    for s in l:          
        if s == 'the':   
            count += 1   
    return count         





# How many "basic operations" in the worst and best case?
def is_member(l: list, ele) -> bool:
    for x in l:          
        if x == ele:     
            return True  
    return False         







# How many "basic operations" in the worst and best case?
def distinct(the_list: list) -> list:
    seen = []
    for element in the_list:      
        if element not in seen:   
            seen.append(element)  
    return seen






# An alternative that uses a set
def distinct_set(the_list: list) -> set:
    seen = set()
    for element in the_list:        
        seen.add(element)
    return seen
# (Compare runtime)






###################################################################
# This part of the program allows me to run it as a script in class
# I've added comments for your reference, in case you're interested,
# but it's not strictly part of the class material today.
###################################################################
if __name__ == '__main__':
    # The "sys" library lets us look at the arguments given in the terminal
    import sys
    # "sys.argv" is the number of arguments (including the Python file name)
    # Different languages handle this differently; print out the value if you're curious.
    if(len(sys.argv) < 3):
        # Informative error message!
        raise ValueError('When running this script, please give the name of the file to open, then count_the, distinct, or distinct_set.')
    # The Python file name always comes first (index 0). So the *text* file name is at [1]
    file_to_open = sys.argv[1]
    # And the function to run is in [2]. 
    function_to_run = sys.argv[2]
    opened_file = open(file_to_open, 'r', encoding='utf8')
    text = opened_file.read()
    # Notice that we need to connect the string data that says which function to run
    # with the actual function name. That's what this if-elif-else is for. 
    # (If you're curious, there are cleaner ways to set this connection up, but we 
    #  haven't covered them yet in 0112... ask me about them if you're curious.)
    if function_to_run == "count_the":
        count = count_the(text.split())
        print(f'That file had {count} appearances of the word "the".')   
    elif function_to_run == "distinct":
        uniques = distinct(text.split())
        print(f'That file had {len(uniques)} unique words (including caps, punctuation, etc).')
    elif function_to_run == "distinct_set":
        uniques = distinct_set(text.split())
        print(f'That file had {len(uniques)} unique words (including caps, punctuation, etc). Computed via set.')
    else:
        raise ValueError("Unknown function to run. Please use 'count_the', 'distinct' or 'distinct_set'.")




