# This isn't needed if you're not using typechecking
from typing import Union

class ListNode:
    def __init__(self, data):
        self.data = data
        # If you're using typechecking, you'll need to label this as _either_ 
        #   None or a ListNode:
        self.next: Union[None, ListNode] = None
        # otherwise, there's no need, and you can just do this:
        # self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    # internal helper method, not called from outside the class
    # we'll use the double-underscore convention to label this as "private"
    def __append_to(self, node: ListNode, data):
        if not node.next:
            node.next = ListNode(data)
        else:
            self.__append_to(node.next, data)

    # this is the method that a caller would invoke
    def append(self, data):
        '''Append an element to this linked list'''
        if not self.first:
            self.fst = ListNode(data)
        else:
            self.__append_to(self.first, data)
