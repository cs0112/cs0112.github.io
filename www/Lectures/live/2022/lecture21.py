from typing import Union

# internal implementation detail
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# outside-facing class for others to use
class LinkedList:
    def __init__(self):
        self.first: Union[None, ListNode] = None

    # We could (at the moment) directly access the "first" field.
    # But by convention we probably would want to make that private (__first)
    # Let's make a method to help users get the first element...
    def firstElement(self):
        if not self.first:
            return None # or raise an exception... (next time)
        else:
            return self.first.data

    # internal helper to recursively move to end of list before inserting
    # __ is Python convention for "meant to be private to this class and not invoked by user"
    def __append_to(self, node, new_node):
        if not node.next:
            node.next = new_node
        else:
            self.__append_to(node.next, new_node)

    # outside-facing method for our developer-user to call
    def append(self, data):
        new_node = ListNode(data)
        if not self.first: # None will make this eval to False
            self.first = new_node
        else:
            self.__append_to(self.first, new_node)

    def __length_from(self, node):
        if not node.next:
            return 1
        else:
            return 1 + self.__length_from(node.next)

    def __len__(self): # make our class work with Python's "len(...)"
        # Q: Conceptual parallel between this as adding to the end of the list?
        if not self.first: 
            return 0
        else:
            return self.__length_from(self.first)

    def ith_recursive(self, target: int): 
        '''Returns the i-th element of the list. E.g., if i==0, returns
           the first element of the list. If there is no i-th element, 
           <FILL!> <return None?>
        '''

        def __ith_from(node: ListNode, travelled: int):
            if target == travelled:
                return node.data
            elif not node.next:
                return None            
            else: 
                return __ith_from(node.next, travelled + 1)

        # the _recursive structure_ should be the same as in append/__append_to
        # although the operations will differ. What will those differences look like?
        if not self.first: 
            return None # come back here re: exceptions
        else:
            return __ith_from(self.first, 0)

    def ith_loop(self, target: int):
        location = self.first
        travelled = 0
        while location.next != None:
            if travelled == target: return location
            location = location.next
            travelled = travelled + 1
            # ...










l = LinkedList()
l.append('A')
l.append('B')
l.append('C')
print(len(l))

# don't do this:
#print(l.__length_from(l.first))