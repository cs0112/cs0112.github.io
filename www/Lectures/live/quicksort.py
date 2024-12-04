
# Dataclasses won't let you include both fields in == but only one 
# field in <, >, etc. So we'll use a normal class for this.
class Record: 
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    def __ne__(self, other):
        if other == None: return False
        return self.age != other.age or self.name != other.name
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    # is this correct?
    def __ge__(self, other):
        return self.age >= other.age
    def __le__(self, other):
        return self.age <= other.age
    def __repr__(self):
        return f'Record({self.age}, {self.name})'








# One last sorting algorithm: what if we prefer the sorting to be 
# more explicit than it is in merge sort, but we want to keep the 
# divide-and-conquer approach?
def quick_sort(l: list) -> list:
    '''Sort the input list and return a sorted copy.'''
    if len(l) <= 1: 
        return l[:]
    # pick a value from the list we're sorting
    pivot = l[0]
    smaller = [x for x in l if x < pivot]
    larger = [x for x in l if x > pivot]
    same = [x for x in l if not (x < pivot or x > pivot)]
    smaller_sorted = quick_sort(smaller)
    larger_sorted = quick_sort(larger)
    return smaller_sorted + same + larger_sorted
