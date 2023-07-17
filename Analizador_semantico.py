from analizador_sintactico import ast_parsed
from analizador_sintactico import symbol_table


def analyze_semantics(ast_parsed, symbol_table):
    def evaluate_expression(node):
        if node.value.isdigit():
            return int(node.value)
        elif node.value in symbol_table.symbols:
            return symbol_table.get(node.value)
        elif node.value == '+':
            left_value = evaluate_expression(node.children[0])
            right_value = evaluate_expression(node.children[1])
            return left_value + right_value
        else:
            raise ValueError(f"Invalid expression: {node.value}")

    def analyze_node(node):
        if node.value == '=':
            identifier = node.children[0].value
            value = evaluate_expression(node.children[1])
            symbol_table.assign(identifier, value)
        elif node.value == 'print':
            identifier = node.children[0].value
            value = symbol_table.get(identifier)
            print("Comprobacion de la suma de a y b: " + str(value))
        else:
            for child in node.children:
                analyze_node(child)

    analyze_node(ast_parsed)

try:
    print("\n\n\nAnalisis semantico exitoso.")
    analyze_semantics(ast_parsed, symbol_table)
    print("\n\n\nSymbol table:", symbol_table.symbols)
except SyntaxError as e:
    print("Syntax error:", str(e))
