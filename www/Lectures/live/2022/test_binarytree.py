from binarytree import * 

def test_add():
    tree = BST()
    assert tree.add(5) == True
    assert tree.add(9) == True
    assert tree.add(5) == False
    assert tree.add(2) == True

def test_contains():
    tree = BST()
    tree.add(5)
    tree.add(9)
    tree.add(5)
    tree.add(2)
    assert 2 in tree
    assert 5 in tree    
    assert 9 in tree
    assert 17 not in tree

