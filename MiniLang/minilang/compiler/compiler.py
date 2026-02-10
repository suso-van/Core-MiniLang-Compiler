from minilang.parser.ast import *
from minilang.lexer.token import TokenType
from .bytecode import OpCode, Instruction


class Compiler:
    def __init__(self):
        self.instructions = []
        self.functions = {}

    # --------------------------------------------------
    # Emit instruction
    # --------------------------------------------------
    def emit(self, opcode, operand=None):
        self.instructions.append(Instruction(opcode, operand))

    # --------------------------------------------------
    # Main compile dispatcher
    # --------------------------------------------------
    def compile(self, node):

        # ================= Program =================
        if isinstance(node, Program):
            for stmt in node.statements:
                self.compile(stmt)
            self.emit(OpCode.HALT)

        # ================= Let =================
        elif isinstance(node, LetStatement):
            self.compile(node.value)
            self.emit(OpCode.STORE_VAR, node.name)

        # ================= Assign =================
        elif isinstance(node, AssignStatement):
            self.compile(node.value)
            self.emit(OpCode.STORE_VAR, node.name)

        # ================= Print =================
        elif isinstance(node, PrintStatement):
            self.compile(node.expression)
            self.emit(OpCode.PRINT)

        # ================= Number =================
        elif isinstance(node, Number):
            self.emit(OpCode.PUSH_CONST, node.value)

        # ================= Identifier =================
        elif isinstance(node, Identifier):
            self.emit(OpCode.LOAD_VAR, node.name)

        # ================= Binary Operation =================
        elif isinstance(node, BinaryOp):
            self.compile(node.left)
            self.compile(node.right)

            op = node.op.type

            if op == TokenType.PLUS:
                self.emit(OpCode.ADD)
            elif op == TokenType.MINUS:
                self.emit(OpCode.SUB)
            elif op == TokenType.MUL:
                self.emit(OpCode.MUL)
            elif op == TokenType.DIV:
                self.emit(OpCode.DIV)
            elif op == TokenType.LT:
                self.emit(OpCode.LT)
            elif op == TokenType.GT:
                self.emit(OpCode.GT)
            elif op == TokenType.EQ:
                self.emit(OpCode.EQ)
            else:
                raise Exception(f"Unsupported operator: {op}")

        # ================= If =================
        elif isinstance(node, IfStatement):
            self.compile(node.condition)

            jump_false_pos = len(self.instructions)
            self.emit(OpCode.JUMP_IF_FALSE, None)

            self.compile(node.then_branch)

            if node.else_branch:
                jump_end_pos = len(self.instructions)
                self.emit(OpCode.JUMP, None)

                # patch false jump → else
                self.instructions[jump_false_pos].operand = len(self.instructions)
                self.compile(node.else_branch)

                # patch end jump → after else
                self.instructions[jump_end_pos].operand = len(self.instructions)
            else:
                self.instructions[jump_false_pos].operand = len(self.instructions)

        # ================= Block =================
        elif isinstance(node, Block):
            for stmt in node.statements:
                self.compile(stmt)

        # ================= While =================
        elif isinstance(node, WhileStatement):
            loop_start = len(self.instructions)

            self.compile(node.condition)

            jump_false_pos = len(self.instructions)
            self.emit(OpCode.JUMP_IF_FALSE, None)

            self.compile(node.body)
            self.emit(OpCode.JUMP, loop_start)

            # patch false jump → after loop
            self.instructions[jump_false_pos].operand = len(self.instructions)

        # ================= Function Definition =================
        elif isinstance(node, FunctionDef):
            func_start = len(self.instructions)
            self.functions[node.name] = func_start

            # mark function entry
            self.emit(OpCode.FUNC_START, None)

            # store parameters (pop from stack)
            for param in reversed(node.params):
                self.emit(OpCode.STORE_VAR, param)

            for stmt in node.body.statements:
                self.compile(stmt)

            # default return 0
            self.emit(OpCode.PUSH_CONST, 0)
            self.emit(OpCode.RETURN)

            # patch FUNC_START skip address
            self.instructions[func_start].operand = len(self.instructions)

        # ================= Return =================
        elif isinstance(node, ReturnStatement):
            self.compile(node.value)
            self.emit(OpCode.RETURN)

        # ================= Function Call =================
        elif isinstance(node, CallExpression):
            # push args
            for arg in node.args:
                self.compile(arg)

            if node.name not in self.functions:
                raise Exception(f"Undefined function: {node.name}")

            # jump to FUNC_START
            self.emit(OpCode.CALL, self.functions[node.name])

        # ================= Unknown =================
        else:
            raise Exception(f"Unknown AST node: {type(node)}")

        return self.instructions


