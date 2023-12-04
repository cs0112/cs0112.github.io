import pytest
from linkedlist import *

#### STUDENTS
# We have provided you with a very BASIC example of testing for linkedlist. 
# Please expand this testing along with testing for your own methods.
####
def test_init():
    """
    Test the initialization of the LinkedList class.
    """
    ## testing correctt initialization of a LinkedList object
    l = LinkedList()
    assert not l.first


def test_append():
    """
    Test the 'append' method of the LinkedList class. This method should add new nodes to 
    the end of the list, updating the 'next' attributes of the nodes accordingly.
    """
    ## testing append method works on a new LinkedList object
    l = LinkedList()
    l.append("hello")
    assert l.first.data == "hello"
    

def test_length():
    """
    Test the 'length' method of the LinkedList class. This method calculates the number of 
    elements/nodes in the list.
    """
    ## testing the length of a new LinkedList object is 0
    l = LinkedList()
    assert l.length() == 0


def test_nth():
    """
    Test the 'nth' method of the LinkedList class. The 'nth' method retrieves the nth element.
    """
    ## tests retrieval of nth element when linkedlist object is new (empty)
    l = LinkedList()
    with pytest.raises(Exception):
        l.nth(0)


def test_remove():
    """tests the remove function"""
    pass

def test_remove_from():
    """tests the remove_from function"""
    pass


