from typing import Union
# Let's build a binary-tree data structure!

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left: Union[None, BSTNode] = None
        self.right: Union[None, BSTNode] = None
    def __repr__(self):
        '''Discuss: is this a good __repr__?'''
        return self.data

class BST: 
    def __init__(self):
        self.root = None

    # Q: why is this (admittedly odd) helper function useful?
    def __search(self, node: BSTNode, data) -> BSTNode:
        '''Finds the BSTNode in the tree rooted at <node> that either
          (a) contains the data value; or
          (b) is the last node visited on an unsuccessful search for the value             
        '''
        if node.data < data and node.right != None: 
            return self.__search(node.right, data)
        elif node.data > data and node.left != None:
            return self.__search(node.left, data)
        else: 
            return node
            
    def __contains__(self, data) -> bool:
        if self.root == None: return False
        last_visited = self.__search(self.root, data)
        if last_visited.data == data: return True
        else: return False

    def add(self, data) -> bool:
        '''Add the data value to the tree. If the value is already in the 
           tree, the tree won't be modified (i.e., we forbid duplicates).
           
           If the value is inserted, the function returns True. 
           Otherwise, the function returns False.'''
        if self.root == None:
            self.root = BSTNode(data)
            return True
        else:
            last_visited = self.__search(self.root, data)
            if last_visited.data < data: 
                last_visited.right = BSTNode(data)
                return True
            elif last_visited.data > data:
                last_visited.left = BSTNode(data)
                return True
            else: # last_visited.data == data
                return False

    def __traverse_dfs(self, node: BSTNode) -> list:
        '''Depth-first traversal of the tree'''
        # "pre-order traversal"
        # [my value][left subtree's values][right subtree's values]
        # example: [7, 5, 3, 6, 12, 10, 17]
        #result = [node.data]
        result = []
        if node.left != None:
            result = result + self.__traverse_dfs(node.left)
        # "in-order traversal"
        # [left subtree's values][my value][right subtree's values]       
        # example: [3,5,6,7,10,12,17]   
        result = result + [node.data]      
        if node.right != None:
            result = result + self.__traverse_dfs(node.right)
        return result

    def __repr__(self):
        if self.root == None:
            return 'BST([])'
        else:
            return 'BST('+str(self.__traverse_dfs(self.root))+')'

    ## added 2023 -- won't work with a traverse that returns values not nodes
    def __validate(self, subroot):
        '''For debugging / development only: validate the BST invariant 
           after every tree-modifying operation is completed. This is 
           expensive, but a useful trick for catching errors. E.g., the 
           algorithm for adding a new value works locally, but is the 
           implementation itself? Maybe we made a mistake!'''
        if subroot.left != None:
            for child in self.__traverse_dfs(subroot.left):
                if child.data > subroot.data:
                    raise Exception(f'invariant failed: {child.data} > {subroot.data}') 
                self.__validate(child)
        if subroot.right != None:
            for child in self.__traverse_dfs(subroot.right):
                if child.data < subroot.data:
                    raise Exception(f'invariant failed: {subroot.data} > {child.data}')
                self.__validate(child)

def demo():
    tree = BST()
    tree.add(7)
    tree.add(5)
    tree.add(12)
    tree.add(3)
    tree.add(6)
    tree.add(10)
    tree.add(17)
    print(tree)
demo()