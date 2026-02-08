from minilang.lexer.lexer import Lexer
from minilang.parser.parser import Parser
from minilang.parser.ast_printer import ASTPrinter
from minilang.compiler.compiler import Compiler
from minilang.vm.vm import VirtualMachine
from minilang.semantic.semantic_analyzer import SemanticAnalyzer

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

# ----- Semantic Analysis -----
semantic = SemanticAnalyzer()
semantic.analyze(ast)

# ----- Bytecode -----
print("\n===== BYTECODE =====")
compiler = Compiler()
bytecode = compiler.compile(ast)
for i, instr in enumerate(bytecode):
    print(f"{i}: {instr}")

# ----- VM -----
print("\n===== VM OUTPUT =====")
vm = VirtualMachine(bytecode)
vm.run()

# ----- Use Before Declaration -----
print("\n===== USE BEFORE DECLARATION =====")
code5 = "print(x);"
lexer5 = Lexer(code5)
parser5 = Parser(lexer5)
ast5 = parser5.parse()
semantic5 = SemanticAnalyzer()
try:
    semantic5.analyze(ast5)
except Exception as e:
    print(e)

# ----- Duplicate Variable -----
print("\n===== DUPLICATE VARIABLE =====")
code6 = """
let x = 5;
let x = 10;
"""
lexer6 = Lexer(code6)
parser6 = Parser(lexer6)
ast6 = parser6.parse()
semantic6 = SemanticAnalyzer()
try:
    semantic6.analyze(ast6)
except Exception as e:
    print(e)

# ----- While loop (0..4) -----
print("\n===== WHILE LOOP (0..4) =====")
code_while = """
let x = 0;

while (x < 5) {
    print(x);
    let x = x + 1;
}
"""
lexer_w = Lexer(code_while)
parser_w = Parser(lexer_w)
ast_w = parser_w.parse()
semantic_w = SemanticAnalyzer()
semantic_w.analyze(ast_w)
compiler_w = Compiler()
bytecode_w = compiler_w.compile(ast_w)
vm_w = VirtualMachine(bytecode_w)
vm_w.run()

