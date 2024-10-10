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
    pass

print(count_words(frankenstein_data))
