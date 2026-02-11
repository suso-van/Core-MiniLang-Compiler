from minilang.parser.ast import *


class Optimizer:

    def optimize(self, node):
        if isinstance(node, Program):
            node.statements = [self.optimize(s) for s in node.statements]
            return node

        elif isinstance(node, BinaryOp):
            left = self.optimize(node.left)
            right = self.optimize(node.right)

            if isinstance(left, Number) and isinstance(right, Number):
                if node.op.type.name == "PLUS":
                    return Number(left.value + right.value)
                if node.op.type.name == "MINUS":
                    return Number(left.value - right.value)
                if node.op.type.name == "MUL":
                    return Number(left.value * right.value)
                if node.op.type.name == "DIV":
                    return Number(left.value // right.value)

            node.left = left
            node.right = right
            return node

        elif isinstance(node, LetStatement):
            node.value = self.optimize(node.value)
            return node

        elif isinstance(node, PrintStatement):
            node.expression = self.optimize(node.expression)
            return node

        return node
