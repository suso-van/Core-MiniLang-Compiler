# MiniLang Compiler

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Status](https://img.shields.io/badge/Project-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Compiler](https://img.shields.io/badge/Type-Bytecode%20Compiler-orange)
![VM](https://img.shields.io/badge/VM-Stack%20Based-red)

A fully functional **compiler + virtual machine** implemented from scratch in Python.  
MiniLang demonstrates real compiler architecture including **lexical analysis → parsing → semantic analysis → bytecode generation → execution**.

This project is designed to mirror how real production compilers and runtime systems work while remaining readable and educational.

---

## Overview

MiniLang is a custom programming language executed on a **stack-based virtual machine**.  
The project implements the complete compilation pipeline and supports variables, arithmetic, control flow, semantic validation, and bytecode execution.

---

## Features

- Custom programming language (MiniLang)
- Lexer (Tokenizer)
- Recursive-descent Parser
- Abstract Syntax Tree (AST)
- Semantic Analyzer (Symbol Table + Error Checking)
- Bytecode Compiler
- Stack-Based Virtual Machine
- Control Flow:
  - `let` variables
  - Arithmetic operations
  - Comparisons (`< > ==`)
  - `print()`
  - `if / else`
  - `while` loops
- Error Detection:
  - Use before declaration
  - Duplicate variables
  - Invalid syntax
- Clean bytecode execution
- End-to-end execution via `main.py`

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
│   └── utils/
│
├── main.py
└── README.md
```
---

## Example Program

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
## Compiler Pipeline

MiniLang follows real compiler architecture:

1. **Lexer** → Converts source code into tokens  
2. **Parser** → Builds Abstract Syntax Tree  
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

## Run the Project

### Requirements
Python 3.9+

### Execute
```bash
cd MiniLang
python3 main.py
```

---

## Error Handling

MiniLang detects semantic errors such as:

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
- Stack-based VM execution
- Control flow (if / while)
- Symbol table & semantic checks
- Bytecode interpreter
- Real compiler architecture

---

## Roadmap

- Functions & Call Stack
- Scope System
- Optimizer (constant folding)
- Bytecode Serialization
- REPL (Interactive Shell)
- Standard Library
- Garbage Collection
- JIT Compilation (Experimental)

---

## Educational Value

This project demonstrates:

- Compiler Engineering
- Virtual Machine Design
- Bytecode Execution Models
- Symbol Tables & Semantic Analysis
- Control Flow Compilation
- Runtime Systems

Ideal for:

- Systems programming learners  
- Compiler & language enthusiasts  
- Backend / infrastructure engineers  
- Interview-level architecture preparation  

---

## License

MIT License
