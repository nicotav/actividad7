class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, identifier, value=None):
        if identifier in self.symbols:
            raise ValueError(f"Variable '{identifier}' already declared")
        self.symbols[identifier] = value

    def assign(self, identifier, value):
        if identifier not in self.symbols:
            raise ValueError(f"Variable '{identifier}' not declared")
        self.symbols[identifier] = value

    def get(self, identifier):
        if identifier not in self.symbols:
            raise ValueError(f"Variable '{identifier}' not declared")
        return self.symbols[identifier]
    


