from .ast import *


class ASTPrinter:
    def print(self, node, indent=0):
        space = "  " * indent

        # ================= PROGRAM =================
        if isinstance(node, Program):
            print(f"{space}Program")
            for stmt in node.statements:
                self.print(stmt, indent + 1)

        # ================= LET =================
        elif isinstance(node, LetStatement):
            print(f"{space}LetStatement: {node.name}")
            self.print(node.value, indent + 1)

        # ================= ASSIGN =================
        elif isinstance(node, AssignStatement):
            print(f"{space}AssignStatement: {node.name}")
            self.print(node.value, indent + 1)

        # ================= PRINT =================
        elif isinstance(node, PrintStatement):
            print(f"{space}PrintStatement")
            self.print(node.expression, indent + 1)

        # ================= NUMBER =================
        elif isinstance(node, Number):
            print(f"{space}Number: {node.value}")

        # ================= IDENTIFIER =================
        elif isinstance(node, Identifier):
            print(f"{space}Identifier: {node.name}")

        # ================= BINARY =================
        elif isinstance(node, BinaryOp):
            print(f"{space}BinaryOp: {node.op.type.name}")
            self.print(node.left, indent + 1)
            self.print(node.right, indent + 1)

        # ================= BLOCK =================
        elif isinstance(node, Block):
            print(f"{space}Block")
            for stmt in node.statements:
                self.print(stmt, indent + 1)

        # ================= IF =================
        elif isinstance(node, IfStatement):
            print(f"{space}If")
            self.print(node.condition, indent + 1)
            self.print(node.then_branch, indent + 1)
            if node.else_branch:
                self.print(node.else_branch, indent + 1)

        # ================= WHILE =================
        elif isinstance(node, WhileStatement):
            print(f"{space}While")
            self.print(node.condition, indent + 1)
            self.print(node.body, indent + 1)

        # ================= FUNCTION DEF =================
        elif isinstance(node, FunctionDef):
            params = ", ".join(node.params)
            print(f"{space}FunctionDef: {node.name}({params})")
            self.print(node.body, indent + 1)

        # ================= RETURN =================
        elif isinstance(node, ReturnStatement):
            print(f"{space}Return")
            self.print(node.value, indent + 1)

        # ================= CALL =================
        elif isinstance(node, CallExpression):
            print(f"{space}Call: {node.name}")
            for arg in node.args:
                self.print(arg, indent + 1)

        # ================= UNKNOWN =================
        else:
            print(f"{space}Unknown node: {type(node)}")
