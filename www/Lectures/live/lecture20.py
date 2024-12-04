# Linked lists!

# empty 
# link(1, empty)
# link(1, link(2, empty))

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next: ListNode | None = None
    def __str__(self):
        if not self.next:
            return f'{self.data}'
        else: 
            return f'{self.data},{str(self.next)}'

class LinkedListIterator:
    def __init__(self, current_node: ListNode | None):
        self.current_node = current_node
    def __next__(self):
        if self.current_node == None: 
            raise StopIteration()
        to_return = self.current_node.data
        self.current_node = self.current_node.next
        return to_return
    def __iter__(self):
        return self


# The entire list, containing various public-facing methods,
# the reference to the first link in the list, and so on...
class LinkedList:
    def __init__(self): 
        self.first = None
    def __str__(self):
        return f'[{self.first}]'
    
    def __search(self, current_location, item):
        if item == current_location.data:
            return True
        # otherwise, we need to search...
        if current_location.next == None: 
            return False
        else: 
            return self.__search(current_location.next, item)
        
    def __contains__(self, item): 
        if not self.first: 
            return False
        else:
            return self.__search(self.first, item)

    def __iter__(self):
        return LinkedListIterator(self.first)

    def append(self, data): 
        '''Add a new value to the end of the list.'''
        if not self.first: 
            self.first = ListNode(data)
        else: 
            self.__append_to(self.first, ListNode(data))
    
    def __append_to(self, current_location: ListNode, to_add: ListNode):
        if not current_location.next:
            current_location.next = to_add
        else: 
            self.__append_to(current_location.next, to_add)

    def __length_from(self, current_location: ListNode):
        if not current_location.next: 
            return 1
        else:
            return 1 + self.__length_from(current_location.next)

    def __len__(self):
        if not self.first:
            return 0
        else:
            return self.__length_from(self.first)
        


empty = LinkedList()
one_element = LinkedList()
one_element.append('hello!')
two_elements = LinkedList()
two_elements.append(1)
two_elements.append(2)
print(empty)
print(one_element)
print(two_elements)
three_elements = LinkedList()
three_elements.append(1)
three_elements.append(2)
three_elements.append(3)
print(three_elements)

# why not write this? why don't I like it? (it passes!)
# it's good for testing __str__, but not for other applications
assert str(three_elements) == '[1,2,3]'

assert len(three_elements) == 3
assert len(two_elements) == 2
assert len(one_element) == 1
assert len(empty) == 0

assert 1 in three_elements
assert 2 in three_elements
assert 3 in three_elements
assert 4 not in three_elements

for value in three_elements:
    print(f'in three_elements: {value}')
for value in three_elements:
    print(f'in three_elements: {value}')