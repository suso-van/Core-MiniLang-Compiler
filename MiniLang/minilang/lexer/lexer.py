from .token import Token, TokenType, KEYWORDS


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current = text[0] if text else None

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current = None
        else:
            self.current = self.text[self.pos]

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def number(self):
        start = self.pos
        while self.current and self.current.isdigit():
            self.advance()
        return int(self.text[start:self.pos])

    def identifier(self):
        start = self.pos
        while self.current and (self.current.isalnum() or self.current == "_"):
            self.advance()
        value = self.text[start:self.pos]
        token_type = KEYWORDS.get(value, TokenType.IDENT)
        return value, token_type

    def next_token(self):
        while self.current:

            if self.current.isspace():
                self.skip_whitespace()
                continue

            if self.current.isdigit():
                return Token(TokenType.NUMBER, self.number(), self.pos)

            if self.current.isalpha() or self.current == "_":
                value, ttype = self.identifier()
                return Token(ttype, value, self.pos)

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

            if self.current == "=":
                self.advance()
                return Token(TokenType.ASSIGN, "=", self.pos)

            if self.current == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(", self.pos)

            if self.current == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")", self.pos)

            if self.current == ";":
                self.advance()
                return Token(TokenType.SEMICOLON, ";", self.pos)

            raise Exception(f"Illegal character: {self.current}")

        return Token(TokenType.EOF, None, self.pos)
