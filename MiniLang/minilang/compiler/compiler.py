from minilang.parser.ast import *
from minilang.lexer.token import TokenType
from .bytecode import OpCode, Instruction


class Compiler:
    def __init__(self):
        self.instructions = []
        self.functions = {}

    # --------------------------------------------------
    # Emit helper
    # --------------------------------------------------
    def emit(self, opcode, operand=None):
        self.instructions.append(Instruction(opcode, operand))

    # --------------------------------------------------
    # Compile dispatcher
    # --------------------------------------------------
    def compile(self, node):

        # ================= PROGRAM =================
        if isinstance(node, Program):
            for stmt in node.statements:
                self.compile(stmt)
            self.emit(OpCode.HALT)

        # ================= LET =================
        elif isinstance(node, LetStatement):
            self.compile(node.value)
            self.emit(OpCode.STORE_VAR, node.name)

        # ================= ASSIGN =================
        elif isinstance(node, AssignStatement):
            self.compile(node.value)
            self.emit(OpCode.STORE_VAR, node.name)

        # ================= PRINT =================
        elif isinstance(node, PrintStatement):
            self.compile(node.expression)
            self.emit(OpCode.PRINT)

        # ================= NUMBER =================
        elif isinstance(node, Number):
            self.emit(OpCode.PUSH_CONST, node.value)

        # ================= IDENTIFIER =================
        elif isinstance(node, Identifier):
            self.emit(OpCode.LOAD_VAR, node.name)

        # ================= BINARY =================
        elif isinstance(node, BinaryOp):
            self.compile(node.left)
            self.compile(node.right)

            t = node.op.type
            if t == TokenType.PLUS:
                self.emit(OpCode.ADD)
            elif t == TokenType.MINUS:
                self.emit(OpCode.SUB)
            elif t == TokenType.MUL:
                self.emit(OpCode.MUL)
            elif t == TokenType.DIV:
                self.emit(OpCode.DIV)
            elif t == TokenType.LT:
                self.emit(OpCode.LT)
            elif t == TokenType.GT:
                self.emit(OpCode.GT)
            elif t == TokenType.EQ:
                self.emit(OpCode.EQ)
            else:
                raise Exception("Unsupported binary operator")

        # ================= BLOCK =================
        elif isinstance(node, Block):
            for stmt in node.statements:
                self.compile(stmt)

        # ================= IF =================
        elif isinstance(node, IfStatement):
            self.compile(node.condition)

            jf = len(self.instructions)
            self.emit(OpCode.JUMP_IF_FALSE, None)

            self.compile(node.then_branch)

            if node.else_branch:
                je = len(self.instructions)
                self.emit(OpCode.JUMP, None)

                self.instructions[jf].operand = len(self.instructions)
                self.compile(node.else_branch)
                self.instructions[je].operand = len(self.instructions)
            else:
                self.instructions[jf].operand = len(self.instructions)

        # ================= WHILE =================
        elif isinstance(node, WhileStatement):
            start = len(self.instructions)
            self.compile(node.condition)

            jf = len(self.instructions)
            self.emit(OpCode.JUMP_IF_FALSE, None)

            self.compile(node.body)
            self.emit(OpCode.JUMP, start)

            self.instructions[jf].operand = len(self.instructions)

        # ================= FUNCTION DEF =================
        elif isinstance(node, FunctionDef):
            func_entry = len(self.instructions)
            self.functions[node.name] = func_entry

            # Skip function body in normal execution
            self.emit(OpCode.FUNC_START, None)

            # Bind parameters (pop args into variables)
            for param in reversed(node.params):
                self.emit(OpCode.STORE_VAR, param)

            # Compile body
            self.compile(node.body)

            # Default return 0 if no explicit return
            self.emit(OpCode.PUSH_CONST, 0)
            self.emit(OpCode.RETURN)

            # Patch skip address
            self.instructions[func_entry].operand = len(self.instructions)

        # ================= RETURN =================
        elif isinstance(node, ReturnStatement):
            self.compile(node.value)
            self.emit(OpCode.RETURN)

        # ================= CALL =================
        elif isinstance(node, CallExpression):
            if node.name not in self.functions:
                raise Exception(f"Undefined function: {node.name}")

            # Push arguments
            for arg in node.args:
                self.compile(arg)

            func_addr = self.functions[node.name]
            argc = len(node.args)

            self.emit(OpCode.CALL, (func_addr, argc))

        else:
            raise Exception(f"Unknown AST node: {type(node)}")

        return self.instructions
