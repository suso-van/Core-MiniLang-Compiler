from minilang.lexer.lexer import Lexer

code = """
let x = 5;
let y = 10;
print(x + y);
"""

lexer = Lexer(code)

while True:
    tok = lexer.next_token()
    print(tok)
    if tok.type.name == "EOF":
        break
    
from minilang.lexer.lexer import Lexer
from minilang.parser.parser import Parser

code = """
let x = 5;
let y = 10;
print(x + y);
"""

lexer = Lexer(code)
parser = Parser(lexer)

ast = parser.parse()
print(ast)
