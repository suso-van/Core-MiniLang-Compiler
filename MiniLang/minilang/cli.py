import sys
from minilang.lexer.lexer import Lexer
from minilang.parser.parser import Parser
from minilang.compiler.compiler import Compiler
from minilang.vm.vm import VirtualMachine


def run_file(path):
    with open(path, "r") as f:
        code = f.read()

    lexer = Lexer(code)
    parser = Parser(lexer)
    ast = parser.parse()

    compiler = Compiler()
    bytecode = compiler.compile(ast)

    vm = VirtualMachine(bytecode)
    vm.run()


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m minilang.cli <file>")
        sys.exit(1)

    run_file(sys.argv[1])


if __name__ == "__main__":
    main()
