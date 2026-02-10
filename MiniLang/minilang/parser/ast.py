class Program:
    def __init__(self, statements):
        self.statements = statements


class Block:
    def __init__(self, statements):
        self.statements = statements


class LetStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintStatement:
    def __init__(self, expression):
        self.expression = expression


class IfStatement:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class WhileStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class Number:
    def __init__(self, value):
        self.value = value


class Identifier:
    def __init__(self, name):
        self.name = name


class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class AssignStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class FunctionDef:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body


class ReturnStatement:
    def __init__(self, value):
        self.value = value


class CallExpression:
    def __init__(self, name, args):
        self.name = name
        self.args = args
