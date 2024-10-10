# Fall 2023 live-code template 

frankenstein_file = open('frankenstein.txt', 'r', encoding='utf8')
print(frankenstein_file) 
frankenstein_data = frankenstein_file.read()

bruno_data = frankenstein_data.replace("Frankenstein", "Bruno")
print(bruno_data)
bruno_file = open('bruno.txt', 'w')
bruno_file.write(bruno_data)
bruno_file.close()

def count_words(s: str) -> dict:
    """
    Accepts a string and returns a dictionary that maps words to the number of times 
    each word appears in the string. 
    """
    result = {}
    words: list = s.split()
    for word in words: 
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result

example_input = "Welcome   to cs 112, Welcome"
example_output = {"Welcome": 2, 
                  "to": 1, 
                  "cs": 1, 
                  "112": 1} 

print(count_words(example_input))

print(count_words(example_input) == example_output)

def most_common(counts: dict) -> str:
    most_common = '' # bad naming :-(
    most_common_count = 0
    for word in counts:   
        if counts[word] > most_common_count:    
            most_common = word
            most_common_count = counts[word]
    return most_common

if __name__ == '__main__':
    print(most_common(count_words(frankenstein_data)))





# NOTE: The line below assumes VSCode is opened to the folder this file is located in. 
# You can also run "python3 lecture02.py" in the terminal without this problem.
# NOTE: Depending on your operating system and setup, you might need to provide an 
#   encoding type as well. I've added it below.
# frankenstein_file = open('frankenstein.txt', 'r')
# frankenstein_file = open('frankenstein.txt', 'r', encoding='utf8')

# print(frankenstein_file) # *not* the text itself
# frankenstein_text = frankenstein_file.read()
# print(frankenstein_text) # the text itself


# def count_words(s: str) -> dict: 
#     pass # "pass" in Python means "do nothing" 

# example_input: str = "Why do I feel bitter when I should be feeling sweet?"
# example_output: dict = {"Why": 1, "do": 1, "I": 2, "bitter": 1, "when": 1,
#                         "should": 1, "be": 1, "feeling": 1, "feel": 1, "sweet?": 1}






# print(count_words(example_input))
# assert count_words(example_input) == example_output




# print(count_words(frankenstein_text))
