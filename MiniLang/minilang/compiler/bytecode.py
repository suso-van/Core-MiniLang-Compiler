from enum import Enum, auto


class OpCode(Enum):
    # ---------- Stack ----------
    PUSH_CONST = auto()
    LOAD_VAR = auto()
    STORE_VAR = auto()

    # ---------- Arithmetic ----------
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()

    # ---------- Compare ----------
    LT = auto()
    GT = auto()
    EQ = auto()

    # ---------- Control ----------
    JUMP = auto()
    JUMP_IF_FALSE = auto()

    # ---------- IO ----------
    PRINT = auto()

    # ---------- Functions ----------
    CALL = auto()
    RETURN = auto()
    FUNC_START = auto()

    # ---------- Program ----------
    HALT = auto()


class Instruction:
    def __init__(self, opcode, operand=None):
        self.opcode = opcode
        self.operand = operand

    def __repr__(self):
        if self.operand is None:
            return f"{self.opcode.name}"
        return f"{self.opcode.name} {self.operand}"
