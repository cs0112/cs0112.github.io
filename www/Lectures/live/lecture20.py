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
    # def __repr__(self):
    #     return f'{self.data},{repr(self.next)}'

# intuition:
# zeronode = ListNode(0)
# onenode = ListNode(1)
# zeronode.next = onenode

class LinkedList:
    def __init__(self):
        # Reference to the first ListNode object in the chain of links 
        # (I.e., the first element of the list)
        self.first = None
        self.count = 0

    def __collect_data(self, next_node) -> list:
        if next_node.next == None:  
            return [next_node.data]
        else: 
            return [next_node.data] + self.__collect_data(next_node.next)

    def to_python_list(self):
        if self.first == None: 
            return []
        else: 
            return self.__collect_data(self.first)

    def __repr__(self):
        return repr(self.to_python_list())
    
    def __len__(self):
        return self.count

    def __append_to(self, next_node, data):
        '''Iterate through the linked list starting at ((next_node)) 
        until we find the last element, and then add a new list node 
        for this data.'''
        if next_node.next == None: 
            new_node = ListNode(data)
            next_node.next = new_node
            self.count += 1
        else: 
            self.__append_to(next_node.next,data)
    def append(self, data):
        if not self.first:          
            self.first = ListNode(data)
            self.count += 1
        else:
            self.__append_to(self.first, data)

my_list = LinkedList()
print(my_list)
my_list.append(1)
print(my_list)
my_list.append(2)
print(my_list)
my_list.append(3)
print(my_list)
print(len(my_list))
#print(my_list.first.next.next.next.data)


# What else can we write? 
#   prepend
#   len
#   nth (get element at index n)
#   str/repr, eq, ...