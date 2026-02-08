class Node:
    pass


class Program(Node):
    def __init__(self, statements):
        self.statements = statements


class LetStatement(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintStatement(Node):
    def __init__(self, expression):
        self.expression = expression


class Number(Node):
    def __init__(self, value):
        self.value = value


class Identifier(Node):
    def __init__(self, name):
        self.name = name


class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class If(Node):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
