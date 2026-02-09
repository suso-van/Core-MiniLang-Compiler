from enum import Enum


class TokenType(Enum):
    # literals / identifiers
    IDENT = "IDENT"
    NUMBER = "NUMBER"

    # keywords
    LET = "LET"
    PRINT = "PRINT"
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"

    # operators
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    DIV = "/"

    ASSIGN = "="
    EQ = "=="
    LT = "<"
    GT = ">"

    # symbols
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    SEMICOLON = ";"

    EOF = "EOF"


class Token:
    def __init__(self, type_, value, position):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {self.value}, position={self.position})"
