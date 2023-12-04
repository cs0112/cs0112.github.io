# Live code Nov 3, 2023
# Let's implement Binary Search Trees!
 
from typing import Union

class BSTNode:
    '''Internal class to represent a node in the BST. 
       Not for public use.'''
    def __init__(self, data):
        self.data = data 
        # If you have type-hint checking on, you may need something like 
        # these types, which say left and right can be *either* None or 
        # a BSTNode.
        self.left: Union[None, BSTNode] = None
        self.right: Union[None, BSTNode] = None
    def __repr__(self):
        return self.data
    
class BST: 
    '''Class implementing a binary search tree'''
    def __init__(self):
        self.root = None

    def add(self, data):
        '''Add a (new) value to the tree. If it is already there, 
        return False. Otherwise, return True.'''
        if self.root == None: 
            self.root = BSTNode(data)
            return True
        
        result = self.__descend(data, self.root)
        if result.data == data: 
            return False  # didn't add anything
        elif result.data > data:
            ## RESULT.LEFT HAD BETTER BE NONE!!!!!!!!!!11111
            result.left = BSTNode(data)
            return True
        else: 
            ## DITTO RESULT.RIGHT!!!!!11
            result.right = BSTNode(data)
            return True

    def __descend(self, data, node):
        '''Performs a BST search, returns either the node containing
        the target data or the LAST node visited in the descent.'''
        if data == node.data: 
            return node
        elif data < node.data:
            # go left!
            if node.left == None: 
                return node
            else: 
                # pass the message back up!
                return self.__descend(data, node.left)
        else:
            # go right!
            if node.right == None: 
                return node
            else: 
                # pass the message back up!
                return self.__descend(data, node.right)
    
    def search(self, data):
        '''Search for data within the tree, returns it if found, otherwise None'''
        if self.root == None: 
            return None # False would be OK too, but read on
        result = self.__descend(data, self.root)
        if result.data == data:
            return result.data 
        else: 
            return None

    # Blurring str() vs. repr() distinction
    def __repr__(self):
        if self.root == None:
            return 'BST([])'
        else: 
            return f'BST({self.__collect(self.root)})'
        
    def __collect(self, node) -> list:
        #partial_result = [node.data] # PRE-ORDER (debugging, rep. structure, ...)
        partial_result = []
        if node.left != None: 
            # partial_result.append(self.__collect(node.left))
            partial_result += self.__collect(node.left)

        partial_result.append(node.data) # IN-ORDER (for sorting!)

        if node.right != None:
            # partial_result.append(self.__collect(node.right))
            partial_result += self.__collect(node.right)
        return partial_result
        
        
    
bst = BST()
bst.add(3)
bst.add(1)
bst.add(5)
bst.add(7)
bst.add(4)

print(bst)