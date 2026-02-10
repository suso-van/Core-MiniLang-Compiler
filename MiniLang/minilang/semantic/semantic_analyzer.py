from minilang.parser.ast import *


class SemanticAnalyzer:
    def __init__(self):
        self.symbols = {}
        self.functions = {}

    def analyze(self, node):

        # ---------------- PROGRAM ----------------
        if isinstance(node, Program):
            for stmt in node.statements:
                self.analyze(stmt)

        # ---------------- LET ----------------
        elif isinstance(node, LetStatement):
            if node.name in self.symbols:
                raise Exception(f"Semantic Error: Variable '{node.name}' already declared")
            self.analyze(node.value)
            self.symbols[node.name] = True

        # ---------------- ASSIGN ----------------
        elif isinstance(node, AssignStatement):
            if node.name not in self.symbols:
                raise Exception(f"Semantic Error: Variable '{node.name}' used before declaration")
            self.analyze(node.value)

        # ---------------- IDENT ----------------
        elif isinstance(node, Identifier):
            if node.name not in self.symbols:
                raise Exception(f"Semantic Error: Variable '{node.name}' used before declaration")

        # ---------------- NUMBER ----------------
        elif isinstance(node, Number):
            pass

        # ---------------- BINARY ----------------
        elif isinstance(node, BinaryOp):
            self.analyze(node.left)
            self.analyze(node.right)

        # ---------------- PRINT ----------------
        elif isinstance(node, PrintStatement):
            self.analyze(node.expression)

        # ---------------- IF ----------------
        elif isinstance(node, IfStatement):
            self.analyze(node.condition)
            self.analyze(node.then_branch)
            if node.else_branch:
                self.analyze(node.else_branch)

        # ---------------- WHILE ----------------
        elif isinstance(node, WhileStatement):
            self.analyze(node.condition)
            self.analyze(node.body)

        # ---------------- BLOCK ----------------
        elif isinstance(node, Block):
            for stmt in node.statements:
                self.analyze(stmt)

        # ================= FUNCTION SUPPORT =================

        # ---------- FUNCTION DEF ----------
        elif isinstance(node, FunctionDef):
            if node.name in self.functions:
                raise Exception(f"Semantic Error: Function '{node.name}' already defined")

            self.functions[node.name] = node

            # New local scope for parameters
            old_symbols = self.symbols.copy()

            for param in node.params:
                self.symbols[param] = True

            self.analyze(node.body)

            # Restore scope
            self.symbols = old_symbols

        # ---------- FUNCTION CALL ----------
        elif isinstance(node, CallExpression):
            if node.name not in self.functions:
                raise Exception(f"Semantic Error: Function '{node.name}' not defined")

            for arg in node.args:
                self.analyze(arg)

        # ---------- RETURN ----------
        elif isinstance(node, ReturnStatement):
            self.analyze(node.value)

        else:
            raise Exception(f"Semantic Error: Unknown node in semantic analysis: {type(node)}")
