from Analizador_semantico import symbol_table, ast_parsed


class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []

    def generate_code(self, ast):
        self.traverse_ast(ast)
        return self.code

    def traverse_ast(self, node):
        if node.value == '=':
            identifier = node.children[0].value
            expression = self.generate_expression_code(node.children[1])
            self.code.append(f"{identifier} = {expression}")
        elif node.value == 'print':
            identifier = node.children[0].value
            self.code.append(f"print({identifier})")
        else:
            for child in node.children:
                self.traverse_ast(child)

    def generate_expression_code(self, node):
        if node.value.isdigit():
            return node.value
        elif node.value in self.symbol_table.symbols:
            return node.value
        elif node.value == '+':
            left_expression = self.generate_expression_code(node.children[0])
            right_expression = self.generate_expression_code(node.children[1])
            return f"{left_expression} + {right_expression}"
        else:
            raise ValueError(f"Invalid expression: {node.value}")

    def set_symbol_table(self, symbol_table):
        self.symbol_table = symbol_table



try:

    generator = IntermediateCodeGenerator()
    generator.set_symbol_table(symbol_table)
    intermediate_code = generator.generate_code(ast_parsed)

    print("\n\n\nIntermediate Code:")
    for line in intermediate_code:
        print(line)

except SyntaxError as e:
    print("Syntax error:", str(e))
