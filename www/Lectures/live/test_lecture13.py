from lecture13 import *
from htmltree import *

def test_count_tag():
    # Find the number of <li> tags within <html></html>
    example_tree_1 = HTMLTree("html", [], "")
    assert parse("<html></html>") == example_tree_1
    assert count_tag(parse("<html></html>"), "li") == 0
    assert count_tag(parse("<html></html>"), "html") == 1
    example_tree_2 = HTMLTree("html", [HTMLTree("table", [], ''), HTMLTree("table", [], '')], "")
    assert count_tag(parse("<html><table></table><table></table></html>"), "table") == 2
    
    # from class!
    assert count_tag(parse("<html><table><table></table></table></html>"), "table") == 2
    assert count_tag(parse("<html><table></table><html><table><table></table></table></html></html>"), "table") == 3


def test_all_text():
    pass

