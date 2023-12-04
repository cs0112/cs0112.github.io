
# Dataclasses won't let you include both fields in == but only one 
# field in <, >, etc. So we'll use a normal class for this.
class Record: 
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    def __ne__(self, other):
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
    # ??? what should we do here? if we're combining with +, probably it's not the same
    # as it was in merge sort.
    pivot = l[0] # arbitrary choice! could be many others...
    side1 = [x for x in l if x < pivot]
    # ? Do we like this? Could we fix it differently?
    same = [x for x in l if not (x < pivot) and not (x > pivot)]
    side2 = [x for x in l if x > pivot]
    side1_sorted = quick_sort(side1)
    side2_sorted = quick_sort(side2)
    return side1_sorted + same + side2_sorted
