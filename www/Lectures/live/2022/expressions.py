class Value:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "Value({})".format(self.value)
    def __str__(self):
        return str(self.value)
    def interp(self):
        return self

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
    def interp(self):
        if self.op == '+':
            return self.left.interp() + self.right.interp()
        if self.op == '-':
            return self.left.interp() - self.right.interp()
        if self.op == '*':
            return self.left.interp() * self.right.interp()
        if self.op == '/':
            return self.left.interp() / self.right.interp()
        raise ValueError(self.op)

print(Value(5).interp())
print(Operation('+', Value(5), Value(6)).interp())
print(Operation('+', Operation('/', 2, 1), Value(2)).interp())
