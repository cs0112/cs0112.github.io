from lecture06 import cast_of_chars

def test_cast_of_chars():  
  assert cast_of_chars("") == set()
  assert cast_of_chars("Tim") == {"TIM"}
  assert cast_of_chars("Hello, Hello") == {"HELLO"}
  assert cast_of_chars("hi there abc") == set()
  assert cast_of_chars("tIM") == set() 
