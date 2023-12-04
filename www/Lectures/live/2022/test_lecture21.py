from lecture21 import *

# We cannot do much with the lists yet except appending. So let's just make 
# sure these don't crash; we'll confirm the append is working next time.
def test_append():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    # print(lst) # notice this isn't very informative yet!
    assert len(lst) == 2

def test_ith():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    assert lst.ith_recursive(0) == 1
    assert lst.ith_recursive(1) == 2
    assert lst.ith_recursive(3) == None
    assert lst.ith_recursive(-1) == None
