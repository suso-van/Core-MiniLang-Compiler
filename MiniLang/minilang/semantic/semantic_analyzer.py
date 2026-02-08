from minilang.parser.ast import *
from .symbol_table import SymbolTable


class SemanticAnalyzer:
    def __init__(self):
        self.symbols = SymbolTable()

    def analyze(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.analyze(stmt)

        elif isinstance(node, LetStatement):
            self.analyze(node.value)
            self.symbols.define(node.name)

        elif isinstance(node, PrintStatement):
            self.analyze(node.expression)

        elif isinstance(node, Identifier):
            if not self.symbols.exists(node.name):
                raise Exception(
                    f"Semantic Error: Variable '{node.name}' used before declaration"
                )

        elif isinstance(node, BinaryOp):
            self.analyze(node.left)
            self.analyze(node.right)

        elif isinstance(node, Number):
            pass

        elif isinstance(node, If):
            self.analyze(node.condition)
            self.analyze(node.then_branch)
            if node.else_branch:
                self.analyze(node.else_branch)

        elif isinstance(node, While):
            self.analyze(node.condition)
            self.analyze(node.body)

        elif isinstance(node, Block):
            self.symbols.push_scope()
            for stmt in node.statements:
                self.analyze(stmt)
            self.symbols.pop_scope()

        else:
            raise Exception(f"Unknown node in semantic analysis: {type(node)}")
