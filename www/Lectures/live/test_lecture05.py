from lecture05 import add_len_to_list

# def add_len_to_list(lst: list):
#     lst.append(len(lst))

def test_add_len_to_list_empty():
    # wrong shape of test! append modifies the list
    # assert add_len_to_list([]) == [0]
    test_list = []
    add_len_to_list(test_list)
    assert len(test_list) == 1
    assert test_list[0] == 0
    assert test_list == [0]
    assert not (test_list is [0])

def test_add_len_to_list_singleton():
    test_list = [0]
    add_len_to_list(test_list)
    assert test_list == [0,1]
