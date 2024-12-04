# Let's implement binary search trees! 

# Our board example, except without lines between nodes:
#            7
#        5       12
#      3   6   10  17

class BSTNode:
    def __init__(self, data):
        self.data = data 
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None
    def __str__(self):
        return f'({self.data}, {str(self.left)},{str(self.right)})'
    
class BST:
    def __init__(self): 
        self.root = None
        self.count = 0
    
    def __str__(self):
        # Perhaps we can do better, here? 
        return str(self.__collect_dfs(self.root, 'pre'))
    
    def __len__(self): 
        # This *RELIES UPON* everyone using `add` to add to the tree
        # If they access our root and modify the tree themselves, we are 
        # in trouble -- counter is out of sync
        return self.count

    def add(self, data):
        new_node = BSTNode(data)
        if self.root == None:
            self.root = new_node
            self.count = self.count + 1
        else:  
            # Find either a node with this data, OR the node we 
            # visited, right before falling off the tree
            stopped = self.__search(self.root, data)
            if stopped.data == data:
                pass
            elif stopped.data > data:
                self.count = self.count + 1
                stopped.left = new_node
            else:
                self.count = self.count + 1
                stopped.right = new_node

    def add_list(self, a_list): 
        '''Add every element of the list to this BST'''
        # This is bad! Want to sort, then take middle, recursively
        for ele in a_list: 
            self.add(ele)
        pass

    def __contains__(self, target_value): 
        if self.root == None: 
            return False
        else:
            stopped = self.__search(self.root, target_value)
            return stopped.data == target_value

    def __search(self, current_node: BSTNode, target_value) -> BSTNode:
        '''Starting from <current_node>, searching for either:
           - the first node found containing <target_value>; or 
           - the last node visited, if <target_value> is not found.'''
        if target_value == current_node.data:
            return current_node # found it! return it!
        elif target_value < current_node.data:
            # move left (if we can!)
            if current_node.left == None:
                return current_node
            else: 
                return self.__search(current_node.left, target_value)
        else:
            # move right (if we can)
            if current_node.right == None:
                return current_node
            else: 
                return self.__search(current_node.right, target_value)

    # For myself, in reality, I'd probably put the debug stuff in another method, and not 
    # complicate this one. Avoiding lots of code re-use is good, but avoiding complexity 
    # is also good. There are also cleaner ways to add the `order` option.
    def __collect_dfs(self, current: BSTNode | None, order: str, debug: bool = False):
        '''Produce a list of all the values stored in the binary search tree rooted in <current>.
           Follows a depth-first traversal pattern. Pass "in", "pre", or "post" for 
           in-order, pre-order, or post-order traversal respectively.'''
        if current == None: 
            return []
        result = []
        if order == 'pre': result.append(current.data)
        if current.left != None: 
            if debug: result.append(self.__collect_dfs(current.left, order, debug)) 
            else: result += self.__collect_dfs(current.left, order, debug)            
        if order == 'in': result.append(current.data)
        if current.right != None: 
            if debug: result.append(self.__collect_dfs(current.right, order, debug)) 
            else: result += self.__collect_dfs(current.right, order, debug)
        if order == 'post': result.append(current.data)
        return result
    
    def sort(self):
        '''Return the elements of this tree in lexicographic order.'''
        return self.__collect_dfs(self.root, 'in')
    
    def topological(self):
        '''Return the elements of this tree ordered to respect dependencies.'''
        return self.__collect_dfs(self.root, 'pre')

#            7
#        5       12
#      3   6   10  17
# pre-order: [7, 5, 3, 6, 12, 10, 17]
# in-order:  [3, 5, 6, 7, 10, 12, 17] 

my_tree = BST()
my_tree.add(7)
my_tree.add(6)
my_tree.add(5)
my_tree.add(3)
my_tree.add(17)
my_tree.add(12)
my_tree.add(10)

print(my_tree)
print(5 in my_tree)
print(15 in my_tree)
print(17 in my_tree)