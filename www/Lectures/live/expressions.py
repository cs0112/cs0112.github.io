# Let's write a calculator! We'll start with some classes for the different 
# kinds of expressions we'll need to handle: numbers and operations. 

class Value:
    '''A constant numeric value. E.g., Value(5).'''
    def __init__(self, value: float):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f'Value({repr(self.value)})'
    def interpret(self, environment: dict[str, float]) -> float:
        '''Evaluate this expression and return the (numeric) result.'''
        return self.value

class BinOperator: 
    '''Application of a binary operator like addition, multiplication, etc.'''
    def __init__(self, op, left, right):
        self.op = op 
        self.left = left 
        self.right = right
    def __str__(self):
        return f'({str(self.left)} {str(self.op)} {str(self.right)})'
    def __repr__(self):
        return f'BinOperator({repr(self.op)}, {repr(self.left)}, {repr(self.right)})'
    def interpret(self, environment: dict[str, float]) -> float:
        '''Evaluate this expression and return the (numeric) result.'''
        if self.op == '+': return self.left.interpret(environment) + self.right.interpret(environment)
        if self.op == '-': return self.left.interpret(environment) - self.right.interpret(environment)
        if self.op == '*': return self.left.interpret(environment) * self.right.interpret(environment)
        if self.op == '/': 
            right_value = self.right.interpret(environment)
            # throw our own custom behavior for division by zero
            if right_value == 0:
                raise ValueError(f'denominator was zero for {str(self)}')
            return self.left.interpret(environment) / right_value
        else: raise ValueError(f'illegal operator for BinOperator: {self.op}')

class IfNonzero:
    '''An if-then expression. E.g., IfNonzero(Value(1), Value(2), Value(3)).
       IfNonzero(x,y,z) evaluates to y if x is nonzero, and z otherwise.'''
    def __init__(self, cond, iftrue, iffalse):
        self.cond = cond
        self.iftrue = iftrue
        self.iffalse = iffalse
    def __str__(self):
        return f'if({str(self.cond)}!=0): ({str(self.iftrue)}) else ({str(self.iffalse)})'
    def __repr__(self):
        return f'IfNonzero({repr(self.cond)}, {repr(self.iftrue)}, {repr(self.iffalse)})'
    def interpret(self, environment: dict[str, float]) -> float:
        '''Evaluate this expression and return the (numeric) result.'''
        if self.cond.interpret(environment) != 0: 
            return self.iftrue.interpret(environment)
        else:
            return self.iffalse.interpret(environment)

class Variable:
    '''A variable, to be given a concrete value later.'''
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return f'Variable({repr(self.name)})'
    def interpret(self, environment: dict[str, float]) -> float:
        '''Evaluate this expression and return the (numeric) result.'''
        if self.name in environment:
            return environment[self.name]
        else:
            raise ValueError(f'No value was available for variable: {self.name}')



# We represent expressions as _trees_ here. For instance:

# 1 + 2 is represented as (+ 1 2)
example1  = BinOperator('+', Value(1), 
                             Value(2))
print(example1)
print(example1.interpret({}))

# (2/5)*2 is represented as (* (/ 2 5) 2)
example2 = BinOperator('*', BinOperator('/', Value(2), 
                                             Value(5)), 
                            Value(2))
print(example2)
print(example2.interpret({}))

example3  = BinOperator('+', BinOperator('+', Value(1), 
                                              Value(2)),
                             Value(3))
print(example3)
print(example3.interpret({}))

example4 = BinOperator('/', Value(2),
                            BinOperator('-', Value(2), 
                                             Value(2)))

print(example4)
# print(example4.interpret({}))


example5 = IfNonzero(Value(0),  # BinOperator('+', Value(1), Value(2)), 
                     BinOperator('-', Value(5), Value(6)),
                     BinOperator('/', Value(100), Value(3)))

print(example5)
print(example5.interpret({}))

example6 = BinOperator('/', Variable('x'),
                            BinOperator('-', Value(1), 
                                             Value(2)))

print(example6)
# this errors, since no value for 'x'
# print(example6.interpret({}))
print(example6.interpret({'x': 5}))