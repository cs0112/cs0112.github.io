# Innocent module won't expect circular imports
from scope_a import add1

value = 100
def set_value(x: int):
    # global value # without this global declaration *in this function*
    value = x    # this assignment is to a fresh, local 'value' variable
    print(f'set_value called with: {value}; get_value (inside scope_a) now returns: {get_value()}, id(value): {id(value)}')

# Note: returns value of "value", not a reference
def get_value():
    print(f'get_value; id(value): {id(value)}')
    return value

def write_value_to_file():
    import sys
    my_file = open('test_value.txt', 'w')
    my_file.write(str(value))    
    my_file.close()


if __name__ == '__main__':    
    print(f'inside main (scope_b), id(set_value)={id(set_value)}')
    add1(value)
    print(value)