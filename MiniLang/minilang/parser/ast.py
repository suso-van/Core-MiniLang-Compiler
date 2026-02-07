class AST:
    pass


class Program(AST):
    def __init__(self, statements):
        self.statements = statements


class LetStatement(AST):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintStatement(AST):
    def __init__(self, expression):
        self.expression = expression


class Number(AST):
    def __init__(self, value):
        self.value = value


class Identifier(AST):
    def __init__(self, name):
        self.name = name


class BinaryOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
