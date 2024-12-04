from lecture06 import *

def test_cast_of_chars():
  assert cast_of_chars("") == set()
  assert cast_of_chars("Tim") == {"TIM"}
  assert cast_of_chars("'hello,' said TIM") == {"TIM"}
  assert cast_of_chars("hello Tim hello Tim hello Annabelle") == {"TIM", "ANNABELLE"}
  # This example points out something we might need to _decide on_. Why?
  assert cast_of_chars("hello Tim hello TiM hello Annabelle") == {"TIM", "ANNABELLE"}

# "The cow that was on Harry's farm belonged to Sasha."
# {"THE", "HARRY'S", "SASHA"}

# "Hello, how are you, Marzia, hello?"
# {"HELLO", "MARZIA"}

# "I like my sisters Sara and Sam."
# {"I", "SARA", "SAM."}

# "!Tim!"
# {"TIM"}
