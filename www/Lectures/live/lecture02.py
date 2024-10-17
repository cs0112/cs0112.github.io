# Fall 2023 live-code template 

# NOTE: The line below assumes VSCode is opened to the folder this file is located in. 
# You can also run "python3 lecture02.py" in the terminal without this problem.
frankenstein_file = open('frankenstein.txt', 'r', encoding='utf8')
print(frankenstein_file) 
frankenstein_data = frankenstein_file.read()
print(frankenstein_data) 
bruno = frankenstein_data.replace('Frankenstein', 'Bruno')
bruno_file = open('bruno.txt', 'w', encoding='utf8')
bruno_file.write(bruno)

def count_words(s):     
    """
    Accepts a string and returns a dictionary containing a count of 
    the number of times each word is seen.
    """
    result = {}
    words = s.split()
    for word in words:
        print(result) 
        if word not in result:
            result[word] = 1
        else: 
            result[word] = result[word] + 1
    return result 


example_input: str = "Why do I feel bitter when I should be feeling sweet?"
example_output: dict = {"Why": 1, "do": 1, "I": 2, "bitter": 1, "when": 1,
                        "should": 1, "be": 1, "feeling": 1, "feel": 1, "sweet?": 1}
assert count_words(example_input) == example_output

###################
## FROM SEPTEMBER 9
###################

def most_common(counts: dict):
    """
    Given a dictionary with integer values, returns a key with the 
    highest value in the dictionary.
    """
    most_common_count = 0  # how many times the most common so far seen?
    most_common = ''       # what is the most common so far?    
    for word in counts:   
        if counts[word] > most_common_count:
            # counts[word] is the _value_ stored in the dict for key word
            most_common = word
            most_common_count = counts[word]
    return most_common
    




