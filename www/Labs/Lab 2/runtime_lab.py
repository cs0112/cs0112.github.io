import timeit
import gc

'''
This function appends elements from a list to the list d if d does not yet have the element. The worst-case runtime for this function is quadratic.
'''
def distinct1(l: list) -> list:
    d = []
    for x in l:
        if x not in d:
            d.append(x)
    return d

'''
This function adds elements from a list to the set d if d does not yet have the element. The worst-case runtime for this function is linear.
'''
def distinct2(l: list) -> list:
    d = set()
    for x in l:
        if x not in d:
            d.add(x)
    return d


''' 
This function returns a list which is the best case input to distinct1 and distinct2

The best case input allows distinct1 and distinct2 to run in constant time. This function is returning a list in which all the indices are the same. If n = 3, the list would look as follows: list = [1, 1, 1]

This is the best case input because, since all the elements are the same, something like-- x not in list -- never takes more than a constant number of operations.
'''
def best_case_input(n: int) -> list:
    return [1 for i in range(n)]

''' 
This function reruns a list which is the worst case input to distinct1 and distinct2

It causes distinct1 to work in quadratic time and distinct2 to work in linear time.
    
Try to find which step of distinct1 makes it take longer than distinct2, and write a list which would cause that piece to be slower - that is the list which worst_case_input should return
'''
def worst_case_input(n: int) -> list:
    # TODO: FILL ME IN
    pass

''' 
This method calculates the time it takes a function to run by getting the difference between the end/start times.
'''
def time(fn, arg):
    gc.disable()
    start = timeit.default_timer()
    fn(arg)
    end = timeit.default_timer()
    gc.enable()
    return end - start

'''
This method graphs/plots the runtimes of a function given across different inputs. The graphs will save as images in your current directory.
'''
def graph(name: str, sizes: list, times: list):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.scatter(sizes, times)
    plt.savefig(name + ".png")
    plt.show()
    plt.close()

def generate_graphs():
    '''
    Create a list with 10 different sizes that increment. i.e. 100, 300, 500 etc. Your highest size should not exceed 50000.
    '''
    sizes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # TODO - CHANGE ME

    '''
    Create 2 Graphs that represent the Best Case Graphs (efficient runtimes). 
    
    1. inputs should be a list of lists: call best_case_input() for every size in the sizes list

    2. results1 should be a list with the times it takes to run inputs on the distinct1 function: call the time() function by passing in distinct1 as the function and arg for every arg in inputs

    3. results2 should be a list with the times it takes to run inputs on the distinct2 function: call the time() function by passing in distinct2 as the function and arg for every arg in inputs 
    '''
    inputs = [] # TODO - CHANGE ME
    results1 = [] # TODO - CHANGE ME
    results2 = [] # TODO - CHANGE ME

    # Calling the graph() to save images of the 2 Best Case Graphs
    graph("best1", sizes, results1)
    graph("best2", sizes, results2)

    ''' 
    Create 2 Graphs that represent the Worst Case Graphs (inefficient run times).

    1. inputs should be a list of lists: call worst_case_input() for every size in the sizes list

    2. results1 should be a list with the times it takes to run inputs on the distinct1 function: call the time() function by passing in distinct1 as the function and arg for every arg in inputs

    3. results2 should be a list with the times it takes to run inputs on the distinct2 function: call the time() function by passing in distinct2 as the function and arg for every arg in inputs
    '''
    inputs = [] # TODO - CHANGE ME
    results1 = [] # TODO - CHANGE ME
    results2 = [] # TODO - CHANGE ME

    # Calling graph() to save images of the 2 Worst Case Graphs
    graph("worst1", sizes, results1)
    graph("worst2", sizes, results2)
    

if __name__ == '__main__':
    generate_graphs()
