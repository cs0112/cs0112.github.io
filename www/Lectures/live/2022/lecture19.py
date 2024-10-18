
# outside-facing class for others to use
class LinkedList:
    def __init__(self):
        self.first = None

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

# internal implementation detail
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None