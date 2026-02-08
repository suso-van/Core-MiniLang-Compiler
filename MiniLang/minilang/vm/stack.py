class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.data:
            raise Exception("Stack underflow")
        return self.data.pop()

    def __repr__(self):
        return f"Stack({self.data})"
