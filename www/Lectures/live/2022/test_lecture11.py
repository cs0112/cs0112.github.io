from lecture11 import add, search

def test_single_element():
    table = [[] for _ in range(10)]
    add(table, 'Hi, everybody!')
    assert search(table, 'Hi, everybody!') == True
    # ...once this function returns, `table` disappears
    # future tests can make their own `table` list













def test_single_element_false():
    table = [[] for _ in range(10)]
    add(table, 'Hi, everybody!')    
    assert search(table, 'Bye, nobody!') == False

# Challenge: How does the table work when under excessive load?
#   Not performance; check its functionality

def test_heavy_load():
    table = [[] for _ in range(10)]
    # By "Pigeonhole Principle" we'll have _some_ collisions
    # But _the distribution_ of them is all probabilistic.
    for num in range(100):
        add(table, str(num))   
    for num in range(100):     
        assert search(table, str(num)) == True    
    # ...which means we can't actually know that these 100 elements will hash to
    #  empty or non-empty sublists
    for num in range(100, 200): 
        assert search(table, str(num)) == False
    
# there are techniques for removing the uncertainty; we're learning them in 0320
# not expecting you to use/know them here, but e.g. we can contrive to give our own
# hash function---one that has predictable properties

# (note that if we had _removal_, testing would need to be rather more involved)