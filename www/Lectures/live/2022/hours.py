from lecture13 import *

test5 = parse('<html><emph><strong><p>hello</p></strong></emph><p>hello</p></html>')

def test_count_tag():
    assert count_tag(test5, 'emph') == 1
