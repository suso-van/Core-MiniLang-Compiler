# MiniLang Compiler

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Compiler](https://img.shields.io/badge/Type-Bytecode%20Compiler-orange)
![VM](https://img.shields.io/badge/VM-Stack%20Based-red)

A fully functional **compiler + virtual machine** implemented from scratch in Python.  
MiniLang demonstrates real compiler architecture including:

**Lexical Analysis → Parsing → Semantic Analysis → Bytecode Generation → Virtual Machine Execution**

This project mirrors how real production compilers and runtime systems work while remaining readable and educational.

---

## Overview

MiniLang is a custom programming language executed on a **stack-based virtual machine**.  
The project implements a complete compilation pipeline and supports variables, arithmetic, control flow, functions, recursion, semantic validation, and bytecode execution.

---

## Features

### Language
- Variables (`let`)
- Arithmetic (`+ - * /`)
- Comparisons (`< > ==`)
- `print()` output
- `if / else`
- `while` loops
- Functions
- Recursion

### Compiler Components
- Lexer (Tokenizer)
- Recursive-Descent Parser
- Abstract Syntax Tree (AST)
- Semantic Analyzer (Symbol Table + Error Checking)
- Bytecode Compiler
- Stack-Based Virtual Machine

### Error Detection
- Variable used before declaration
- Duplicate variable declaration
- Invalid syntax
- Stack underflow protection
- Runtime safety checks

---

## Project Structure

```

MiniLang/
│
├── minilang/
│   ├── lexer/        # Tokenizer
│   ├── parser/       # AST + Parser
│   ├── semantic/     # Symbol table + semantic checks
│   ├── compiler/     # Bytecode generator
│   ├── vm/           # Stack virtual machine
│   └── optimizer/    # AST optimizations
│
├── main.py           # Full compiler pipeline runner
└── README.md

````

---

## Example Programs

### Control Flow

```txt
let i = 0;

while (i < 5) {
    if (i == 2) {
        print(999);
    } else {
        print(i);
    }
    i = i + 1;
}
````

Output:

```
0
1
999
3
4
```

---

### Functions

```txt
fn add(a, b) {
    return a + b;
}

let result = add(5, 7);
print(result);
```

Output:

```
12
```

---

### Recursion (Factorial)

```txt
fn fact(n) {
    if (n == 0) { return 1; }
    return n * fact(n - 1);
}

print(fact(5));
```

Output:

```
120
```

---

## Compiler Pipeline

MiniLang follows real compiler architecture:

1. **Lexer** → Converts source code into tokens
2. **Parser** → Builds Abstract Syntax Tree (AST)
3. **Semantic Analyzer** → Validates variables, scope, and usage
4. **Compiler** → Generates stack-based bytecode
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

## How to Run

### Requirements

Python 3.9+

### Execute

```bash
cd MiniLang
python3 main.py
```

This runs built-in test programs demonstrating:

* Variables
* Control flow
* Functions
* Recursion
* Semantic validation

---

## Error Handling

MiniLang detects semantic errors such as:

* Variable used before declaration
* Duplicate variable declaration
* Invalid syntax

Example:

```
Semantic Error: Variable 'x' used before declaration
```

---

## Current Capabilities

* Full compiler pipeline
* Stack-based virtual machine
* Functions + recursion
* Call stack execution
* Control flow compilation
* Symbol table & semantic validation
* Bytecode interpreter
* AST optimizer
* Runtime safety checks

---

## Roadmap (Advanced Systems Features)

* Static type system
* Boolean & string support
* Closures & lexical scope
* Bytecode serialization (.mlbc)
* CLI runner (`minilang program.ml`)
* Interactive REPL
* Debugger / step execution
* Garbage Collection
* Register-based VM
* JIT compilation (research)
* SSA-based optimizer
* Intermediate Representation (IR)

---

## Educational Value

This project demonstrates real **Systems / Compiler Engineering**:

* Compiler Design
* Virtual Machine Architecture
* Stack Execution Model
* Call Stack & Recursion
* Bytecode Generation
* Symbol Tables & Semantic Analysis
* Control Flow Compilation
* Runtime System Design

---

## Suitable For

* GATE CS preparation
* Systems programming portfolio
* Compiler / Language engineering
* Backend / runtime engineering roles
* FAANG / Top-tier system design depth

---

## Core Systems Portfolio

Part of a Core Systems Engineering series:

1. Educational OS Kernel
2. Mini Database Engine
3. Order Matching Engine
4. MiniLang Compiler

---

## License

MIT License


