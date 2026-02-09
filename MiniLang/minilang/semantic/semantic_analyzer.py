from minilang.parser.ast import *

class SemanticAnalyzer:
    def __init__(self):
        self.symbols = set()

    def analyze(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.analyze(stmt)

        elif isinstance(node, LetStatement):
            if node.name in self.symbols:
                raise Exception(f"Semantic Error: Variable '{node.name}' already declared")
            self.symbols.add(node.name)
            self.analyze(node.value)

        elif isinstance(node, AssignStatement):
            if node.name not in self.symbols:
                raise Exception(f"Semantic Error: Variable '{node.name}' not declared")
            self.analyze(node.value)

        elif isinstance(node, PrintStatement):
            self.analyze(node.expression)

        elif isinstance(node, IfStatement):
            self.analyze(node.condition)
            self.analyze(node.then_branch)
            if node.else_branch:
                self.analyze(node.else_branch)

        elif isinstance(node, WhileStatement):
            self.analyze(node.condition)
            self.analyze(node.body)

        elif isinstance(node, Block):
            for stmt in node.statements:
                self.analyze(stmt)

        elif isinstance(node, BinaryOp):
            self.analyze(node.left)
            self.analyze(node.right)

        elif isinstance(node, Identifier):
            if node.name not in self.symbols:
                raise Exception(f"Semantic Error: Variable '{node.name}' used before declaration")

        elif isinstance(node, Number):
            pass

        else:
            raise Exception(f"Unknown node in semantic analysis: {type(node)}")
