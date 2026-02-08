from .ast import *


class ASTPrinter:
    def print(self, node, indent=0):
        prefix = "  " * indent

        # ---------------- Program ----------------
        if isinstance(node, Program):
            print(prefix + "Program")
            for stmt in node.statements:
                self.print(stmt, indent + 1)

        # ---------------- LetStatement ----------------
        elif isinstance(node, LetStatement):
            print(prefix + f"LetStatement: {node.name}")
            self.print(node.value, indent + 1)

        # ---------------- PrintStatement ----------------
        elif isinstance(node, PrintStatement):
            print(prefix + "PrintStatement")
            self.print(node.expression, indent + 1)

        # ---------------- Number ----------------
        elif isinstance(node, Number):
            print(prefix + f"Number: {node.value}")

        # ---------------- Identifier ----------------
        elif isinstance(node, Identifier):
            print(prefix + f"Identifier: {node.name}")

        # ---------------- BinaryOp ----------------
        elif isinstance(node, BinaryOp):
            print(prefix + f"BinaryOp: {node.op.type.name}")
            self.print(node.left, indent + 1)
            self.print(node.right, indent + 1)

        # ---------------- Unknown ----------------
        else:
            print(prefix + f"Unknown node: {type(node)}")
