from mergesort import merge_sort
from random import randint





class Book:
    def __init__(self, author: str, title: str, edition: int):
        self.author  = author
        self.title   = title
        self.edition = edition
    def __eq__(self, other):
        # edition doesn't matter
        return self.author == other.author and self.title == other.title 


book1 = Book('a', 'b', 1)
book2 = Book('a', 'b', 2)
book3 = Book('a', 'b', 3)






class IntWrapper:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val 

    def __gt__(self, other):
        return self.val > other.val 

    def __eq__(self, other):
        return randint(0, 1) == 0 

    def __repr__(self):
        return repr(self.val)

iw = IntWrapper(5)

# print(iw == iw)
# print(iw == iw)
# print(iw == iw)
# print(iw == iw)
# print(iw == iw)
# print(iw == iw)
# print(iw == iw)


nums = [IntWrapper(i) for i in range(10)]
for iw in nums:
    print(f'{iw}:{iw == IntWrapper(5)}')