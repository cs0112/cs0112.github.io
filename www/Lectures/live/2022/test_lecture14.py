from lecture14 import *

# Tip: Use the helper 'parse' to avoid having to construct the tree verbosely. 
# Tip: To word-wrap long lines in Python without violating indentation requirements:
  #  use backslash (avoid any blank space after the backslash!)
  #  or use parentheses, square brackets, etc. to group

def test_replace_text():
  # don't replace in tags
  tree_1 = parse('<html></html>')
  replace_text(tree_1, 'html', 'foo')
  assert tree_1 == \
         parse('<html></html>')
  # ^ Note: you don't *need* the backslash wrapping, but I find it's more clear

  # The below tests will _not_ work as written, because replace_text doesn't return anything.

  # replace at nested depths
  tree_2 = parse('<html><p>hello</p><p><strong>world</strong></p></html>')
  print(tree_2)
  assert replace_text(tree_2, 
                      'hello', 
                      'greetings') == \
         parse('<html><p>greetings</p><p><strong>world</strong></p></html>')         
  # ^ Note: Python will let you manually wrap within parens, like this, but unless == 
  #  is within parens you'll need \ to wrap.
  assert (replace_text(
            parse('<html><p>greetings</p><p><strong>world</strong></p></html>'),
            'world', 
            'fellow students') 
            == 
          parse('<html><p>greetings</p><p><strong>fellow students</strong></p></html>'))
  # ^ Note: This wrapping works, because I put an outer set of parens around the assertion condition
   
  # replace partial words
  assert replace_text(parse('<html>chocolate cake</html>'), 'chocolate', 'dog-safe') == \
         parse('<html>dog-safe cake</html>')   
