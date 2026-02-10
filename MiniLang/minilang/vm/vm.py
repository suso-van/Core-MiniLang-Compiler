from minilang.compiler.bytecode import OpCode


class VirtualMachine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.stack = []
        self.globals = {}
        self.call_stack = []
        self.ip = 0

    def run(self):
        while self.ip < len(self.instructions):
            instr = self.instructions[self.ip]
            op = instr.opcode

            # ---------------- PUSH ----------------
            if op == OpCode.PUSH_CONST:
                self.stack.append(instr.operand)

            elif op == OpCode.LOAD_VAR:
                self.stack.append(self.globals.get(instr.operand, 0))

            elif op == OpCode.STORE_VAR:
                val = self.stack.pop()
                self.globals[instr.operand] = val

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

            # ---------------- JUMPS ----------------
            elif op == OpCode.JUMP:
                self.ip = instr.operand
                continue

            elif op == OpCode.JUMP_IF_FALSE:
                val = self.stack.pop()
                if not val:
                    self.ip = instr.operand
                    continue

            # ================= FUNCTION SUPPORT =================

            # Skip function body in normal flow
            elif op == OpCode.FUNC_START:
                self.ip = instr.operand
                continue

            # Function call
            elif op == OpCode.CALL:
                # Save return address
                self.call_stack.append(self.ip + 1)

                # Jump to function start
                self.ip = instr.operand + 1
                continue

            # Function return
            elif op == OpCode.RETURN:
                ret_val = self.stack.pop() if self.stack else 0

                if not self.call_stack:
                    return

                self.ip = self.call_stack.pop()
                self.stack.append(ret_val)
                continue

            # ---------------- HALT ----------------
            elif op == OpCode.HALT:
                break

            else:
                raise Exception(f"Unknown opcode: {op}")

            self.ip += 1

