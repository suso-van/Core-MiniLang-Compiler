from minilang.lexer.lexer import Lexer
from minilang.parser.parser import Parser
from minilang.parser.ast_printer import ASTPrinter
from minilang.compiler.compiler import Compiler
from minilang.vm.vm import VirtualMachine

code = """
let x = 5;
let y = 10;
print(x + y);
"""

# ----- Tokens -----
print("===== TOKENS =====")
lexer = Lexer(code)
while True:
    tok = lexer.next_token()
    print(tok)
    if tok.type.name == "EOF":
        break

# ----- AST -----
print("\n===== AST =====")
lexer = Lexer(code)
parser = Parser(lexer)
ast = parser.parse()
printer = ASTPrinter()
printer.print(ast)

# ----- Bytecode -----
print("\n===== BYTECODE =====")
lexer = Lexer(code)
parser = Parser(lexer)
ast = parser.parse()
compiler = Compiler()
bytecode = compiler.compile(ast)
for i, instr in enumerate(bytecode):
    print(f"{i}: {instr}")

# ----- VM -----
print("\n===== VM OUTPUT =====")
vm = VirtualMachine(bytecode)
vm.run()
