# Linked lists!

# empty
# link(1, empty)
# link(2, link(1, empty))

# Closer to Pyret:
# class ListNode:
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next

#zeronode = ListNode(0, None)

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# intuition:
# zeronode = ListNode(0)
# onenode = ListNode(1)
# zeronode.next = onenode

class LinkedList:
    def __init__(self): 
        self.first = None

    def __append_to(self, node, data):
        pass
        # what should this do? think: move through
        # the list, find the last element...


    def append(self, data):
        if not self.first:          
            self.first = ListNode(data)
        else:
            self.__append_to(self.first, data)

emptylist = LinkedList()

