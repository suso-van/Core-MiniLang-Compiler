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
    # Main compile entry
    # --------------------------------------------------
    def compile(self, node):

        # ================= PROGRAM =================
        if isinstance(node, Program):
            for stmt in node.statements:
                self.compile(stmt)
            self.emit(OpCode.HALT)
            return self.instructions, self.functions

        # ================= BLOCK =================
        elif isinstance(node, Block):
            for stmt in node.statements:
                self.compile(stmt)

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

        # ================= IDENT =================
        elif isinstance(node, Identifier):
            self.emit(OpCode.LOAD_VAR, node.name)

        # ================= BINARY =================
        elif isinstance(node, BinaryOp):
            self.compile(node.left)
            self.compile(node.right)

            if node.op.type == TokenType.PLUS:
                self.emit(OpCode.ADD)
            elif node.op.type == TokenType.MINUS:
                self.emit(OpCode.SUB)
            elif node.op.type == TokenType.MUL:
                self.emit(OpCode.MUL)
            elif node.op.type == TokenType.DIV:
                self.emit(OpCode.DIV)
            elif node.op.type == TokenType.LT:
                self.emit(OpCode.LT)
            elif node.op.type == TokenType.GT:
                self.emit(OpCode.GT)
            elif node.op.type == TokenType.EQ:
                self.emit(OpCode.EQ)

        # ================= IF =================
        elif isinstance(node, IfStatement):
            self.compile(node.condition)

            jfalse = len(self.instructions)
            self.emit(OpCode.JUMP_IF_FALSE, None)

            self.compile(node.then_branch)

            if node.else_branch:
                jend = len(self.instructions)
                self.emit(OpCode.JUMP, None)

                self.instructions[jfalse].operand = len(self.instructions)
                self.compile(node.else_branch)
                self.instructions[jend].operand = len(self.instructions)
            else:
                self.instructions[jfalse].operand = len(self.instructions)

        # ================= WHILE =================
        elif isinstance(node, WhileStatement):
            start = len(self.instructions)

            self.compile(node.condition)

            jfalse = len(self.instructions)
            self.emit(OpCode.JUMP_IF_FALSE, None)

            self.compile(node.body)
            self.emit(OpCode.JUMP, start)

            self.instructions[jfalse].operand = len(self.instructions)

        # ================= FUNCTION DEF =================
        elif isinstance(node, FunctionDef):
            func_start = len(self.instructions)

            # Store function entry in table
            self.functions[node.name] = (func_start, node.params)

            # FUNC_START placeholder → will patch end addr
            self.emit(OpCode.FUNC_START, None)

            # STORE params (reverse because stack order)
            for p in reversed(node.params):
                self.emit(OpCode.STORE_VAR, p)

            # Compile body
            for stmt in node.body.statements:
                self.compile(stmt)

            # Default return 0 if no explicit return
            self.emit(OpCode.PUSH_CONST, 0)
            self.emit(OpCode.RETURN)

            # Patch FUNC_START operand → function end
            self.instructions[func_start].operand = len(self.instructions)

        # ================= RETURN =================
        elif isinstance(node, ReturnStatement):
            self.compile(node.value)
            self.emit(OpCode.RETURN)

        # ================= FUNCTION CALL =================
        elif isinstance(node, CallExpression):
            for arg in node.args:
                self.compile(arg)

            if node.name not in self.functions:
                raise Exception(f"Undefined function: {node.name}")

            func_addr, params = self.functions[node.name]

            # IMPORTANT → ONLY (addr, argc)
            self.emit(OpCode.CALL, (func_addr, len(node.args)))

        else:
            raise Exception(f"Unknown AST node: {type(node)}")
