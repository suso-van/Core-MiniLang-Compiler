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

    def match(self, token_type):
        if self.current.type == token_type:
            self.eat(token_type)
            return True
        return False

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
        if self.current.type == TokenType.LBRACE:
            return self.block()
        if self.current.type == TokenType.LET:
            return self.let_statement()
        if self.current.type == TokenType.PRINT:
            return self.print_statement()
        if self.match(TokenType.IF):
            return self.if_statement()
        if self.match(TokenType.WHILE):
            return self.while_statement()
        
        elif self.current.type == TokenType.FN:
            return self.function_def()

        elif self.current.type == TokenType.RETURN:
            return self.return_statement()

        elif self.current.type == TokenType.IDENT:
            # Could be assignment: x = expr;
            name = self.current.value
            self.eat(TokenType.IDENT)

            if self.current.type == TokenType.ASSIGN:
               self.eat(TokenType.ASSIGN)
               expr = self.expression()
               self.eat(TokenType.SEMICOLON)
               return AssignStatement(name, expr)

        raise Exception(f"Invalid statement near {self.current}")


    def block(self):
        self.eat(TokenType.LBRACE)
        statements = []
        while self.current.type != TokenType.RBRACE:
            statements.append(self.statement())
        self.eat(TokenType.RBRACE)
        return Block(statements)
        
    def let_statement(self):
        self.eat(TokenType.LET)

        name = self.current.value
        self.eat(TokenType.IDENT)

        self.eat(TokenType.ASSIGN)

    # IMPORTANT: allow function call / expression / binary / number
        expr = self.expression()

        self.eat(TokenType.SEMICOLON)

        return LetStatement(name, expr)


    def print_statement(self):
        self.eat(TokenType.PRINT)
        self.eat(TokenType.LPAREN)
        expr = self.expression()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.SEMICOLON)

        return PrintStatement(expr)

    def if_statement(self):
        self.eat(TokenType.LPAREN)
        condition = self.comparison()
        self.eat(TokenType.RPAREN)
        then_branch = self.block() if self.current.type == TokenType.LBRACE else self.statement()
        else_branch = None
        if self.match(TokenType.ELSE):
            else_branch = self.block() if self.current.type == TokenType.LBRACE else self.statement()
        return IfStatement(condition, then_branch, else_branch)

    def while_statement(self):
        self.eat(TokenType.LPAREN)
        condition = self.comparison()
        self.eat(TokenType.RPAREN)
        body = self.block() if self.current.type == TokenType.LBRACE else self.statement()
        return WhileStatement(condition, body)


    # --------------------------------------------------
    # Expressions
    # --------------------------------------------------
    def comparison(self):
        node = self.expression()
        while self.current.type in (TokenType.LT, TokenType.GT, TokenType.EQ):
            op = self.current
            self.eat(op.type)
            node = BinaryOp(node, op, self.expression())
        return node

    def term(self):
       node = self.factor()

       while self.current.type in (TokenType.MUL, TokenType.DIV):
          op = self.current
          self.eat(op.type)
          node = BinaryOp(node, op, self.factor())

       return node


    def expression(self):
        node = self.term()

        while self.current.type in (
            TokenType.PLUS, TokenType.MINUS,
            TokenType.LT, TokenType.GT, TokenType.EQ
    ):
            op = self.current
            self.eat(op.type)
            node = BinaryOp(node, op, self.term())

        return node

    
    def function_def(self):
        self.eat(TokenType.FN)

        name = self.current.value
        self.eat(TokenType.IDENT)

        self.eat(TokenType.LPAREN)

        params = []
        if self.current.type != TokenType.RPAREN:
            params.append(self.current.value)
            self.eat(TokenType.IDENT)

            while self.current.type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
                params.append(self.current.value)
                self.eat(TokenType.IDENT)

        self.eat(TokenType.RPAREN)

        body = self.block()

        return FunctionDef(name, params, body)
    
    def return_statement(self):
        self.eat(TokenType.RETURN)
        expr = self.expression()
        self.eat(TokenType.SEMICOLON)
        return ReturnStatement(expr)


    def factor(self):
        token = self.current
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(token.value)
        elif token.type == TokenType.IDENT:
            name = token.value
            self.eat(TokenType.IDENT)
            if self.current.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current.type != TokenType.RPAREN:
                    args.append(self.expression())
                    while self.current.type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)
                        args.append(self.expression())
                self.eat(TokenType.RPAREN)
                return CallExpression(name, args)
            return Identifier(name)
        
    # (expression)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expression()
            self.eat(TokenType.RPAREN)
            return node

        else:
          raise Exception(f"Unexpected token: {token}")
