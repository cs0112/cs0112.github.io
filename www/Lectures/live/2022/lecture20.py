from typing import Union

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


# internal implementation detail
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

l = LinkedList()
l.append('A')
l.append('B')
l.append('C')
print(len(l))

# don't do this:
#print(l.__length_from(l.first))