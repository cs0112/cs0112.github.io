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

# The entire list, containing various public-facing methods,
# the reference to the first link in the list, and so on...
class LinkedList:
    def __init__(self): 
        self.first = None
    def __str__(self):
        return f'[{self.first}]'

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

