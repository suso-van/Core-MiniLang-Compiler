class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # stack of scopes

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def define(self, name):
        if name in self.scopes[-1]:
            raise Exception(f"Semantic Error: Variable '{name}' already declared")
        self.scopes[-1][name] = True

    def exists(self, name):
        return any(name in scope for scope in self.scopes)
