from minilang.lexer.token import TokenType
from .ast import *


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current = self.lexer.next_token()

    # --------------------------------------------------
    # Core helpers
    # --------------------------------------------------
    def eat(self, token_type):
        if self.current.type == token_type:
            self.current = self.lexer.next_token()
        else:
            raise Exception(f"Expected {token_type}, got {self.current.type}")

    # --------------------------------------------------
    # Entry
    # --------------------------------------------------
    def parse(self):
        statements = []
        while self.current.type != TokenType.EOF:
            statements.append(self.statement())
        return Program(statements)

    # --------------------------------------------------
    # Statements
    # --------------------------------------------------
    def statement(self):
        # let x = expr;
        if self.current.type == TokenType.IDENT and self.current.value == "let":
            return self.let_statement()

        # print(expr);
        if self.current.type == TokenType.IDENT and self.current.value == "print":
            return self.print_statement()

        raise Exception(f"Invalid statement near {self.current}")

    def let_statement(self):
        self.eat(TokenType.IDENT)  # let

        name = self.current.value
        self.eat(TokenType.IDENT)

        self.eat(TokenType.ASSIGN)
        expr = self.expression()
        self.eat(TokenType.SEMICOLON)

        return LetStatement(name, expr)

    def print_statement(self):
        self.eat(TokenType.IDENT)  # print
        self.eat(TokenType.LPAREN)
        expr = self.expression()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.SEMICOLON)

        return PrintStatement(expr)

    # --------------------------------------------------
    # Expressions
    # --------------------------------------------------
    def expression(self):
        node = self.term()

        while self.current.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current
            self.eat(op.type)
            node = BinaryOp(node, op, self.term())

        return node

    def term(self):
        node = self.factor()

        while self.current.type in (TokenType.MUL, TokenType.DIV):
            op = self.current
            self.eat(op.type)
            node = BinaryOp(node, op, self.factor())

        return node

    def factor(self):
        token = self.current

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(int(token.value))

        if token.type == TokenType.IDENT:
            self.eat(TokenType.IDENT)
            return Identifier(token.value)

        if token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expression()
            self.eat(TokenType.RPAREN)
            return node

        raise Exception("Invalid expression")
