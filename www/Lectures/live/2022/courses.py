import csv

def load_data(filename: str):
    """load a CSV file into a useful format for computation"""
    file = open(filename, encoding="utf8")
    reader = csv.reader(file)
    data = {}
    for row in reader:
        # TODO: do something useful with each row
        # for instance, add or modify an entry in a dictionary
        # a row is a list of data you can index into--for instance,
        # on the first row in the example data, it’s:
        # ["Ashley" , "MATH" , "4"]
        pass
    return data

# TODO: implement this function
def most_taken(data) -> str:
    """
    return the department with the highest total
    number of courses taken by all students
    """
    pass

# TODO: implement this function
def widest_ranging(data) -> str:
    """
    return the name of the student who took the most diverse set of courses from different departments
    """
    pass

# TODO: implement this function
def average_courses(data) -> float:
    """return the average total number of courses taken per student"""
    pass

# TODO: implement this function
def only_once(data) -> list:
    """return all of the departments in which exactly one student took courses"""
    
    pass
        
# This code allows the program to be run as a script.
# You shouldn't need to modify it!
# NOTE(sep14) although _we_ probably should have :-) 
if __name__ == '__main__':
   import sys   
   # the first argument to the script is the CSV filename to load
   if(len(sys.argv) < 2):
      raise ValueError('You must provide a CSV filename when running python3 on this file.')   
   filename = sys.argv[1]
   # the second argument to the script is the name of the function
   function_name = sys.argv[2]
   data = load_data(filename)
   if function_name == "most_taken":
       print(most_taken(data))
   elif function_name == "widest_ranging":
       print(widest_ranging(data))
   elif function_name == "average_courses":
       print(average_courses(data))
   elif function_name == "only_once":
       print(only_once(data))
   else:
       print("Unknown function name")