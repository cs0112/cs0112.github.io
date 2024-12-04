class Value:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "Value({})".format(self.value)
    def __str__(self):
        return str(self.value)
    def interp(self, variable_values):
        return self.value

class Operation:
    def __init__(self, op:str, left, right):
        '''
          Supported operators: '+', '-', '*', '/'
        '''
        self.op = op
        self.left = left
        self.right = right
    def __repr__(self):
        return "Operation({} {} {})".format(self.left, self.op, self.right)
    def __str__(self):
        return "({} {} {})".format(str(self.left), str(self.op), str(self.right))
    def interp(self, variable_values):
        if self.op == '+':
            return self.left.interp(variable_values) + self.right.interp(variable_values)
        if self.op == '-':
            return self.left.interp(variable_values) - self.right.interp(variable_values)
        if self.op == '*':
            return self.left.interp(variable_values) * self.right.interp(variable_values)
        if self.op == '/':
            return self.left.interp(variable_values) / self.right.interp(variable_values)
        raise ValueError(self.op)

print(Value(5).interp({}))
print(Operation('+', Value(5), Value(6)).interp({}))
print(Operation('+', Operation('/', Value(2), Value(1)), Value(2)).interp({}))

class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self): 
        return f'{self.name}'
    def __repr__(self):
        return f'Variable({"self.name"})'
    def interp(self, variable_values):
        return variable_values[self.name]

print(Operation('+', Operation('/', Value(2), Variable('x')), Value(2)).interp({"x": 1}))