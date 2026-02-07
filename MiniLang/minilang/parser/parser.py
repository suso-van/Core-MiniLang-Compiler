from minilang.lexer.token import TokenType
from .ast import *


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current = lexer.next_token()

    def eat(self, token_type):
        if self.current.type == token_type:
            self.current = self.lexer.next_token()
        else:
            raise Exception(f"Expected {token_type}, got {self.current.type}")

    # program -> statement*
    def parse(self):
        statements = []
        while self.current.type != TokenType.EOF:
            statements.append(self.statement())
        return Program(statements)

    # statement -> let | print
    def statement(self):
        if self.current.type == TokenType.LET:
            return self.let_statement()
        elif self.current.type == TokenType.PRINT:
            return self.print_statement()
        else:
            raise Exception("Invalid statement")

    # let x = expr ;
    def let_statement(self):
        self.eat(TokenType.LET)
        name = self.current.value
        self.eat(TokenType.IDENT)
        self.eat(TokenType.ASSIGN)
        value = self.expression()
        self.eat(TokenType.SEMICOLON)
        return LetStatement(name, value)

    # print(expr);
    def print_statement(self):
        self.eat(TokenType.PRINT)
        self.eat(TokenType.LPAREN)
        expr = self.expression()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.SEMICOLON)
        return PrintStatement(expr)

    # expr -> term ((+|-) term)*
    def expression(self):
        node = self.term()
        while self.current.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current.type
            self.eat(op)
            node = BinaryOp(node, op, self.term())
        return node

    # term -> factor ((*|/) factor)*
    def term(self):
        node = self.factor()
        while self.current.type in (TokenType.MUL, TokenType.DIV):
            op = self.current.type
            self.eat(op)
            node = BinaryOp(node, op, self.factor())
        return node

    # factor -> NUMBER | IDENT | (expr)
    def factor(self):
        tok = self.current

        if tok.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(tok.value)

        elif tok.type == TokenType.IDENT:
            self.eat(TokenType.IDENT)
            return Identifier(tok.value)

        elif tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expression()
            self.eat(TokenType.RPAREN)
            return node

        else:
            raise Exception("Invalid syntax")
