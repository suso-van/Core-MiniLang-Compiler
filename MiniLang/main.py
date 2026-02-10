from minilang.lexer.lexer import Lexer
from minilang.parser.parser import Parser
from minilang.parser.ast_printer import ASTPrinter
from minilang.compiler.compiler import Compiler
from minilang.vm.vm import VirtualMachine
from minilang.semantic.semantic_analyzer import SemanticAnalyzer


# ============================================================
# Helper: Run full pipeline
# ============================================================

def run(code, title):
    print(f"\n===== {title} =====")

    # ---------- TOKENS ----------
    print("\n--- TOKENS ---")
    lexer = Lexer(code)
    while True:
        tok = lexer.next_token()
        print(tok)
        if tok.type.name == "EOF":
            break

    # ---------- AST ----------
    print("\n--- AST ---")
    lexer = Lexer(code)              # NEW lexer for parser
    parser = Parser(lexer)           # PASS LEXER (not tokens)
    ast = parser.parse()
    ASTPrinter().print(ast)

    # ---------- SEMANTIC ----------
    semantic = SemanticAnalyzer()
    try:
        semantic.analyze(ast)
    except Exception as e:
        print("\nSemantic Error:", e)
        return

    # ---------- BYTECODE ----------
    print("\n--- BYTECODE ---")
    compiler = Compiler()
    bytecode = compiler.compile(ast)
    for i, instr in enumerate(bytecode):
        print(f"{i}: {instr}")

    # ---------- VM ----------
    print("\n--- VM OUTPUT ---")
    vm = VirtualMachine(bytecode)
    vm.run()


# ============================================================
# BASIC PROGRAM
# ============================================================

code_basic = """
let x = 5;
let y = 10;
print(x + y);
"""
run(code_basic, "BASIC PROGRAM")


# ============================================================
# USE BEFORE DECLARATION
# ============================================================

print("\n===== USE BEFORE DECLARATION =====")
code_error1 = "print(x);"
try:
    parser = Parser(Lexer(code_error1))
    ast = parser.parse()
    SemanticAnalyzer().analyze(ast)
except Exception as e:
    print(e)


# ============================================================
# DUPLICATE VARIABLE
# ============================================================

print("\n===== DUPLICATE VARIABLE =====")
code_error2 = """
let x = 5;
let x = 10;
"""
try:
    parser = Parser(Lexer(code_error2))
    ast = parser.parse()
    SemanticAnalyzer().analyze(ast)
except Exception as e:
    print(e)


# ============================================================
# WHILE LOOP
# ============================================================

code_while = """
let x = 0;

while (x < 5) {
    print(x);
    x = x + 1;
}
"""
run(code_while, "WHILE LOOP (0..4)")


# ============================================================
# IF / ELSE
# ============================================================

code_if = """
let a = 10;

if (a > 5) {
    print(100);
} else {
    print(200);
}
"""
run(code_if, "IF / ELSE")


# ============================================================
# COMBINED CONTROL FLOW
# ============================================================

code_combined = """
let i = 0;

while (i < 5) {
    if (i == 2) {
        print(999);
    } else {
        print(i);
    }
    i = i + 1;
}
"""
run(code_combined, "COMBINED CONTROL FLOW")

print("\n===== FUNCTION TEST =====")

code_func = """
fn add(a, b) {
    return a + b;
}

let result = add(5, 7);
print(result);
"""

run(code_func, "FUNCTION CALL")

