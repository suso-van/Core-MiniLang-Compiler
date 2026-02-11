from minilang.lexer.lexer import Lexer
from minilang.parser.parser import Parser
from minilang.parser.ast_printer import ASTPrinter
from minilang.compiler.compiler import Compiler
from minilang.compiler.optimizer import Optimizer
from minilang.vm.vm import VirtualMachine
from minilang.semantic.semantic_analyzer import SemanticAnalyzer


# ============================================================
# FULL PIPELINE
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

    # ---------- PARSE ----------
    print("\n--- AST ---")
    lexer = Lexer(code)
    parser = Parser(lexer)
    ast = parser.parse()
    ASTPrinter().print(ast)

    # ---------- OPTIMIZER ----------
    optimizer = Optimizer()
    ast = optimizer.optimize(ast)

    # ---------- SEMANTIC ----------
    semantic = SemanticAnalyzer()
    try:
        semantic.analyze(ast)
    except Exception as e:
        print("\nSemantic Error:", e)
        return

    # ---------- COMPILE ----------
    print("\n--- BYTECODE ---")
    compiler = Compiler()
    bytecode, functions = compiler.compile(ast)

    for i, instr in enumerate(bytecode):
        print(f"{i}: {instr}")

    # ---------- VM ----------
    print("\n--- VM OUTPUT ---")
    vm = VirtualMachine(bytecode)

    vm.run()


# ============================================================
# BASIC PROGRAM
# ============================================================

run("""
let x = 5;
let y = 10;
print(x + y);
""", "BASIC PROGRAM")


# ============================================================
# WHILE LOOP
# ============================================================

run("""
let x = 0;

while (x < 5) {
    print(x);
    x = x + 1;
}
""", "WHILE LOOP (0..4)")


# ============================================================
# IF / ELSE
# ============================================================

run("""
let a = 10;

if (a > 5) {
    print(100);
} else {
    print(200);
}
""", "IF / ELSE")


# ============================================================
# COMBINED CONTROL FLOW
# ============================================================

run("""
let i = 0;

while (i < 5) {
    if (i == 2) {
        print(999);
    } else {
        print(i);
    }
    i = i + 1;
}
""", "COMBINED CONTROL FLOW")


# ============================================================
# FUNCTION CALL
# ============================================================

run("""
fn add(a, b) {
    return a + b;
}

let result = add(5, 7);
print(result);
""", "FUNCTION CALL")


# ============================================================
# RECURSION
# ============================================================

run("""
fn fact(n) {
    if (n == 0) { return 1; }
    return n * fact(n - 1);
}

print(fact(5));
""", "RECURSION")
