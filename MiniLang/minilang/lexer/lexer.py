from .token import Token, TokenType


KEYWORDS = {
    "let": TokenType.LET,
    "print": TokenType.PRINT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
}


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current = None
        else:
            self.current = self.text[self.pos]

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def identifier(self):
        start = self.pos
        value = ""
        while self.current and (self.current.isalnum() or self.current == "_"):
            value += self.current
            self.advance()

        token_type = KEYWORDS.get(value, TokenType.IDENT)
        return Token(token_type, value, start)

    def number(self):
        start = self.pos
        value = ""
        while self.current and self.current.isdigit():
            value += self.current
            self.advance()
        return Token(TokenType.NUMBER, int(value), start)

    def next_token(self):
        while self.current:

            if self.current.isspace():
                self.skip_whitespace()
                continue

            if self.current.isalpha() or self.current == "_":
                return self.identifier()

            if self.current.isdigit():
                return self.number()

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
