from htmltree import *
from lecture13 import *

def test_count_tag():
    assert count_tag(HTMLTree('html', []), 'p') == 0
    assert count_tag(parse('<html></html>'), 'p') == 0 
    assert count_tag(parse('<html></html>'), 'html') == 1
    assert count_tag(parse('<html><p>hello</p><strong><p>world</p></strong></html>'), 'p') == 2


def test_all_text():
    pass