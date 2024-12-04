from lecture03 import count_words

# Name the _file_ something starting with "test"
# Name the _function_ something starting with "test"
def test_count_words_lecture_example():
    example_input: str = "Why do I feel bitter when I should be feeling sweet?"
    example_output: dict = {"Why": 1, "do": 1, "I": 2, "bitter": 1, "when": 1,
                        "should": 1, "be": 1, "feel": 1, "sweet?": 1}
    # When this fails, you'll get more useful info than you would outside pytest
    assert count_words(example_input) == example_output

def test_count_words_in_class():
    assert count_words(' ') == {}
    assert count_words('hello hello goodbye goodbye') == {'hello': 2, 'goodbye': 2}
    assert count_words('hello hello, goodbye goodbye') == {'hello': 1, 'hello,': 1, 'goodbye': 2}

