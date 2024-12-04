def add1(x: int) -> int:
    # attacker module needs to import-by-need, avoid cyclic dependency error
    from scope_b import set_value, get_value, value
    print(f'inside add1, id(set_value)={id(set_value)}; id(value)={id(value)}')
    # This won't work for the attack, since set_value isn't written with `global`    
    # 
    value = 3
    print(f'inside add1, get_value produces {get_value()}')
    return x + 1