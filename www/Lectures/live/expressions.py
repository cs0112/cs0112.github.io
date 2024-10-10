# November 27 2023

class Value:
    def __init__(self, value):
        ## TODO: check that value is numeric
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f'Value({repr(self.value)})'
    def interp(self, variable_values: dict):
        return self.value # Value(4) -> 4

class BinOperator: 
    def __init__(self, op, left, right):
        ## TODO: check that "op" is +, -, etc. 
        ## TODO: check that left, right are trees
        self.op = op 
        self.left = left 
        self.right = right
    def __str__(self):
        return f'({str(self.left)} {str(self.op)} {str(self.right)})'
    def __repr__(self):
        return f'BinOperator({repr(self.op)}, {repr(self.left)}, {repr(self.right)})'
    def interp(self, variable_values: dict):
        if self.op == '+':
            return self.left.interp(variable_values) + self.right.interp(variable_values)
        if self.op == '-':
            return self.left.interp(variable_values) - self.right.interp(variable_values)
        if self.op == '*':
            return self.left.interp(variable_values) * self.right.interp(variable_values)
        if self.op == '/':
            return self.left.interp(variable_values) / self.right.interp(variable_values)

class Variable:
    def __init__(self, name):
        ## TODO: check that value is letters
        self.name = name
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return f'Variable({repr(self.name)})'
    def interp(self, variable_values: dict):
        return variable_values[self.name]



example1  = BinOperator('+', Value(1), Value(2))
print(example1.interp({}))
print(BinOperator('/', BinOperator('/', Value(2), Value(5)), Value(2)).interp({}))
example3 = BinOperator('/', BinOperator('/', Value(2), Variable('x')), Value(2))
print(example3.interp({'x': 7}))
print(example3.interp({'x': 1}))
print(example3.interp({'x': 2}))
