#  MiniLang Compiler

A complete educational compiler and virtual machine built from scratch in Python.  
MiniLang demonstrates the full compilation pipeline: lexical analysis, parsing, semantic checking, bytecode generation, and execution on a stack-based virtual machine.

This project mirrors real compiler architecture used in production systems while remaining simple, readable, and extensible.

---

## Features

- Custom programming language (MiniLang)
- Lexer (tokenizer)
- Recursive-descent parser
- AST (Abstract Syntax Tree)
- Semantic analyzer (symbol table + error detection)
- Bytecode compiler
- Stack-based virtual machine
- Control flow support:
  - Variables (`let`)
  - Arithmetic (`+ - * /`)
  - Comparisons (`< > ==`)
  - Print statements
  - `if / else`
  - `while` loops
- Error detection:
  - Use before declaration
  - Duplicate variables
- Clean bytecode execution
- Fully working execution via `main.py`

---

## Project Structure

```
MiniLang/
│
├── minilang/
│   ├── lexer/
│   ├── parser/
│   ├── semantic/
│   ├── compiler/
│   ├── vm/
│   └── utils/
│
├── main.py
└── README.md
```

---

## Example Program

```
let i = 0;

while (i < 5) {
    if (i == 2) {
        print(999);
    } else {
        print(i);
    }
    i = i + 1;
}
```

### Output

```
0
1
999
3
4
```

---

## Compilation Pipeline

MiniLang follows a real compiler architecture:

1. **Lexer** → Converts source code into tokens  
2. **Parser** → Builds AST  
3. **Semantic Analyzer** → Validates variables & scope  
4. **Compiler** → Generates bytecode  
5. **Virtual Machine** → Executes bytecode  

---

## Bytecode Example

```
0: PUSH_CONST 0
1: STORE_VAR i
2: LOAD_VAR i
3: PUSH_CONST 5
4: LT
5: JUMP_IF_FALSE 20
...
20: HALT
```

---

## Running the Project

### Requirements
Python 3.9+

### Run
```
cd MiniLang
python3 main.py
```

---

## Error Handling

MiniLang detects:

- Variable used before declaration  
- Duplicate variable declaration  
- Invalid syntax  

Example:

```
Semantic Error: Variable 'x' used before declaration
```

---

## Current Capabilities

- Full compiler pipeline
- Stack VM execution
- Control flow (if/while)
- Symbol table + semantic checks
- Bytecode interpreter

---

## Next Planned Features

- Functions & call stack
- Scope system
- Optimizer (constant folding)
- Bytecode serialization
- REPL
- Standard library
- Garbage collection
- JIT (experimental)

---

## Educational Value

This project demonstrates:

- Compiler construction
- Virtual machine design
- Language execution models
- Control flow compilation
- Symbol table & semantics
- Bytecode architecture

Suitable for:

- Systems programming learners
- Compiler engineering study
- Backend / infrastructure engineers
- Interview-level architecture understanding

---

## License

MIT License
