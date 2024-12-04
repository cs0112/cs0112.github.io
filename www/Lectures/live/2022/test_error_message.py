from lecture13 import *

test5 = parse('<html></p></html>')

def test_count_tag():
    assert count_tag(test5, 'emph') == 1
