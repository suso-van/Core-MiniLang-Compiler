class Environment:
    def __init__(self):
        self.vars = {}

    def store(self, name, value):
        self.vars[name] = value

    def load(self, name):
        if name not in self.vars:
            raise Exception(f"Undefined variable: {name}")
        return self.vars[name]
