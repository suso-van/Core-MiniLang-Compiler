from minilang.compiler.bytecode import OpCode


class VirtualMachine:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.stack = []
        self.vars = {}
        self.call_stack = []
        self.ip = 0  # instruction pointer

    # -----------------------------------------------------
    # RUN
    # -----------------------------------------------------
    def run(self):
        while self.ip < len(self.bytecode):
            instr = self.bytecode[self.ip]
            op = instr.opcode
            arg = instr.operand

            # ---------------- PUSH CONST ----------------
            if op == OpCode.PUSH_CONST:
                self.stack.append(arg)

            # ---------------- LOAD VAR ----------------
            elif op == OpCode.LOAD_VAR:
                self.stack.append(self.vars.get(arg, 0))

            # ---------------- STORE VAR ----------------
            elif op == OpCode.STORE_VAR:
                if not self.stack:
                    raise RuntimeError("Stack underflow on STORE_VAR")
                self.vars[arg] = self.stack.pop()

            # ---------------- ARITH ----------------
            elif op == OpCode.ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)

            elif op == OpCode.SUB:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)

            elif op == OpCode.MUL:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)

            elif op == OpCode.DIV:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a // b)

            # ---------------- COMPARE ----------------
            elif op == OpCode.LT:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(1 if a < b else 0)

            elif op == OpCode.GT:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(1 if a > b else 0)

            elif op == OpCode.EQ:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(1 if a == b else 0)

            # ---------------- PRINT ----------------
            elif op == OpCode.PRINT:
                print(self.stack.pop())

            # ---------------- JUMP ----------------
            elif op == OpCode.JUMP:
                self.ip = arg
                continue

            # ---------------- JUMP IF FALSE ----------------
            elif op == OpCode.JUMP_IF_FALSE:
                cond = self.stack.pop()
                if cond == 0:
                    self.ip = arg
                    continue

            # ---------------- FUNCTION START ----------------
            elif op == OpCode.FUNC_START:
                # Skip function body during normal execution
                self.ip = arg
                continue

            # ---------------- CALL ----------------
            elif op == OpCode.CALL:
                func_addr, argc = arg

                # collect args
                args = [self.stack.pop() for _ in range(argc)][::-1]

                # save return address
                self.call_stack.append(self.ip + 1)

                # push args back for STORE_VAR in function
                for v in args:
                    self.stack.append(v)

                # jump to function
                self.ip = func_addr + 1
                continue

            # ---------------- RETURN ----------------
            elif op == OpCode.RETURN:
                if not self.call_stack:
                    return
                self.ip = self.call_stack.pop()
                continue

            # ---------------- HALT ----------------
            elif op == OpCode.HALT:
                break

            # ---------------- UNKNOWN ----------------
            else:
                raise RuntimeError(f"Unknown opcode {op}")

            self.ip += 1
