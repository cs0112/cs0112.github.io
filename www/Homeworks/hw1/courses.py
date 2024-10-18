import sys
import csv
from typing import Dict, List, Tuple, Any


def load_data(filename: str) -> Dict[Any, Any]:
    """
    Load a CSV file into a useful format for further analysis.
    
    You have the freedom to choose any dictionary structure that you find
    suitable for organizing the data efficiently. Consider how you'll need
    to access and process this data in the other functions.
    """
    file = open(filename, encoding="utf8") # Open the file
    reader = csv.reader(file) # Read the file
    data = {} # Create a dictionary to store the data

    for row in reader:
        # TODO: Process each row and update your data structure
        # Each row contains: [student_name, department, number_of_courses]
        # For example, the first row in the example data is:
        # ["Ashley", "MATH", "4"]
        # Design your data structure to make later computations efficient
        pass

    return data


def most_taken(data: Dict[Any, Any]) -> str:
    """
    Return the department with the highest total number of courses taken by all students.
    """
    # TODO: Implement this function
    pass


def widest_ranging(data: Dict[Any, Any]) -> str:
    """
    Return the name of the student who took the most diverse set of courses from different departments.
    """
    # TODO: Implement this function
    # Hint: You might want to look at the length of each student's "departments" set
    pass


def average_courses(data: Dict[Any, Any]) -> float:
    """
    Return the average total number of courses taken per student.
    """
    # TODO: Implement this function
    # Hint: You might want to iterate through data["departments"] and keep track of the sum
    pass


def only_once(data: Dict[Any, Any]) -> List[str]:
    """
    Return all of the departments in which exactly one student took courses.
    """
    # TODO: Implement this function
    # Note: Be careful not to count a student multiple times for a department
    # if they've taken multiple courses in that department.
    pass

        
# This code allows the program to be run as a script.
# You shouldn't need to modify it!
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python courses.py <filename> <function_name>")
        sys.exit(1)
    
    filename = sys.argv[1]
    function_name = sys.argv[2]
    
    data = load_data(filename)
    
    functions = {
        "most_taken": most_taken,
        "widest_ranging": widest_ranging,
        "average_courses": average_courses,
        "only_once": only_once
    }
    
    if function_name in functions:
        result = functions[function_name](data)
        print(result)
    else:
        print(f"Unknown function name: {function_name}")
        print(f"Available functions: {', '.join(functions.keys())}")
