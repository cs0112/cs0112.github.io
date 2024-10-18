# Monday starting point: marked up code from Friday

# In livecode, I'll often add "NOTE" annotations _after_ class, to give context.

# NOTE(sep09): In class, I had accidentally opened the wrong folder in my VSCode. The line 
#   below assumes VSCode is opened to the folder this file is located in. You can also
#   run "python3 lecture02.py" in the terminal without this problem. In fact, you can 
#   change the folder VSCode is looking at in the prompt below...
#
# NOTE(sep09): Depending on your operating system and setup, you might need to provide an 
#   encoding type as well. I've added it below.
# frankenstein_file = open('frankenstein.txt', 'r')
frankenstein_file = open('frankenstein.txt', 'r', encoding='utf8')
#print(frankenstein_file) # *not* the text itself
frankenstein_text = frankenstein_file.read()
#print(frankenstein_text) # the text itself

# NOTE(sep09) Lines starting with # in Python are comments. 
#   I'm going to stop the Bruno part from running by adding comments before each line.
# bruno_text = frankenstein_text.replace('Frankenstein', 'Bruno')
# NOTE(sep09): Don't try to use this file path! :-) This was the absolute path to the file on my laptop.
#   If VSCode is opened to the proper folder, you won't need anything but 'bruno.txt'
# bruno_file = open('/Users/tim/repos/cs0112/materials/Lectures/live/bruno.txt', 'a')
# bruno_file.write(bruno_text)
# bruno_file.close()

# What's the most common word in the text of the novel Frankenstein?

# How common are _all_ the words?
# What's the shape of the input? a string, the full text of the book
# What's the shape of the output? a dictionary (words -> counts)
# Try to write the function header:
def count_words(s: str): 
    #pass # ??? "pass" in Python means "do nothing" 
    # NOTE(sep12): the Python setup guide we gave you doesn't enable automatic 
    #  type checking---it's not required! I'm still going to sometimes add type
    #  hints though (here I am saying that "result" is a dictionary) because I think
    #  they're helpful for understanding. I'll enable mouseover info to help
    #  with some questions and exercises, but you are not required to. (If you're
    #  curious about setting it up yourself, I'll talk about that *later* in the semester.)
    result: dict = {}
    words = s.split()
    for word in words:
        if word in result:
            result[word] = result[word] + 1
        else: 
            # first time I've seen this word
            result[word] = 1
    return result

example_input: str = "Why do I feel bitter when I should be feeling sweet?"
example_output: dict = {"Why": 1, "do": 1, "I": 2, "bitter": 1, "when": 1,
                        "should": 1, "be": 1, "feeling": 1, "feel": 1, "sweet?": 1}
print(count_words(example_input))
assert count_words(example_input) == example_output
print(count_words(frankenstein_text))

def most_common(counts): 
  most_common = ''
  most_common_count = 0
  for word in counts:   
    if counts[word] > most_common_count:
      most_common = word
      most_common_count = counts[word]    
  return most_common_count
print(most_common(count_words(frankenstein_text)))
print(most_common(count_words(example_input)))