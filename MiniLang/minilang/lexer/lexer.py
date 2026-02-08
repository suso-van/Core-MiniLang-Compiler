from .token import Token, TokenType


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current = self.text[self.pos] if self.text else None

    # --------------------------------------------------
    # Core
    # --------------------------------------------------
    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current = None
        else:
            self.current = self.text[self.pos]

    def skip_whitespace(self):
        while self.current is not None and self.current.isspace():
            self.advance()

    # --------------------------------------------------
    # Token generators
    # --------------------------------------------------
    def identifier(self):
        start = self.pos
        while self.current is not None and (
            self.current.isalnum() or self.current == "_"
        ):
            self.advance()

        value = self.text[start:self.pos]
        return Token(TokenType.IDENT, value, start)

    def number(self):
        start = self.pos
        while self.current is not None and self.current.isdigit():
            self.advance()

        value = self.text[start:self.pos]
        return Token(TokenType.NUMBER, value, start)

    # --------------------------------------------------
    # Main lexer
    # --------------------------------------------------
    def next_token(self):
        while self.current is not None:

            # Skip whitespace
            if self.current.isspace():
                self.skip_whitespace()
                continue

            # Identifiers
            if self.current.isalpha() or self.current == "_":
                return self.identifier()

            # Numbers
            if self.current.isdigit():
                return self.number()

            # Operators
            if self.current == "+":
                self.advance()
                return Token(TokenType.PLUS, "+", self.pos)

            if self.current == "-":
                self.advance()
                return Token(TokenType.MINUS, "-", self.pos)

            if self.current == "*":
                self.advance()
                return Token(TokenType.MUL, "*", self.pos)

            if self.current == "/":
                self.advance()
                return Token(TokenType.DIV, "/", self.pos)

            if self.current == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(", self.pos)

            if self.current == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")", self.pos)

            if self.current == "{":
                self.advance()
                return Token(TokenType.LBRACE, "{", self.pos)

            if self.current == "}":
                self.advance()
                return Token(TokenType.RBRACE, "}", self.pos)

            if self.current == ";":
                self.advance()
                return Token(TokenType.SEMICOLON, ";", self.pos)

            # Assignment / Equality
            if self.current == "=":
                self.advance()
                if self.current == "=":
                    self.advance()
                    return Token(TokenType.EQ, "==", self.pos)
                return Token(TokenType.ASSIGN, "=", self.pos)

            if self.current == "<":
                self.advance()
                return Token(TokenType.LT, "<", self.pos)

            if self.current == ">":
                self.advance()
                return Token(TokenType.GT, ">", self.pos)

            raise Exception(f"Illegal character: {self.current}")

        return Token(TokenType.EOF, None, self.pos)
