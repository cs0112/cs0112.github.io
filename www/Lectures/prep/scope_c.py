from scope_b import set_value, get_value, write_value_to_file
from scope_a import add1

# Alternative entry point, to allow module caching
if __name__ == '__main__':    
    print(f'inside main (scope_c), id(set_value)={id(set_value)}')
    add1(get_value())
    print(f'end of scope_c, about to exit. get_value() produces: {get_value()}')
    write_value_to_file()
    from scope_b import value
    print(f'inside main (scope_c), id(value)={id(value)}')