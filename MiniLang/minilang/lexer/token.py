from enum import Enum, auto


class TokenType(Enum):
    # Keywords
    LET = auto()
    PRINT = auto()

    # Identifiers / literals
    IDENT = auto()
    NUMBER = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    ASSIGN = auto()

    # Symbols
    LPAREN = auto()
    RPAREN = auto()
    SEMICOLON = auto()

    EOF = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()

    LT = auto()
    GT = auto()
    EQ = auto()

    LBRACE = auto()
    RBRACE = auto()


KEYWORDS = {
    "let": TokenType.LET,
    "print": TokenType.PRINT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
}



class Token:
    def __init__(self, type_, value=None, position=0):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {self.value}, position={self.position})"

    