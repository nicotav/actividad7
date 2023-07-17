from analizador_lexico import tokens
from generador_tabla_simbolos import SymbolTable


class ASTNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"ASTNode({self.value}, {self.children})"

def print_ast(node, indent='', is_last_child=True):
    marker = '└── ' if is_last_child else '├── '
    print(f"{indent}{marker}{node.value}")

    if len(node.children) > 1:
        new_indent = indent + '│   ' if not is_last_child else indent + '    '
    else:
        new_indent = indent + '    '

    for i, child in enumerate(node.children):
        is_last = i == len(node.children) - 1
        print_ast(child, new_indent, is_last)

def parse(tokens):
    def match(token_type):
        nonlocal tokens
        if tokens[0][1] == token_type:
            tokens = tokens[1:]
        else:
            raise SyntaxError(f"Expected {token_type}, found {tokens[0][1]}")

    def factor():
        nonlocal tokens
        if tokens[0][1] == 'IDENTIFIER' or tokens[0][1] == 'NUMBER':
            value = tokens[0][0]
            tokens = tokens[1:]
            return ASTNode(value)
        else:
            raise SyntaxError(f"Expected IDENTIFIER or NUMBER, found {tokens[0][1]}")

    def expression():
        left = factor()
        while tokens[0][1] == 'PLUS':
            match('PLUS')
            right = factor()
            left = ASTNode('+', [left, right])
        return left

    def assignment():
        match('INT')
        identifier = tokens[0][0]
        match('IDENTIFIER')
        match('ASSIGN')
        expr = expression()
        match('SEMICOLON')
        return ASTNode('=', [ASTNode(identifier), expr])

    def statement():
        stmts = []
        while tokens:
            if tokens[0][1] == 'INT':
                stmts.append(assignment())
            elif tokens[0][1] == 'PRINT':
                match('PRINT')
                match('LPAREN')
                identifier = tokens[0][0]
                match('IDENTIFIER')
                match('RPAREN')
                match('SEMICOLON')
                stmts.append(ASTNode('print', [ASTNode(identifier)]))
            else:
                raise SyntaxError(f"Unexpected token {tokens[0][1]}")
        return ASTNode('Program', stmts)

    ast = statement()
    return ast


def build_symbol_table(ast):
    symbol_table = SymbolTable()

    def traverse_ast(node):
        if node.value == '=':
            identifier = node.children[0].value
            symbol_table.declare(identifier)
        elif node.value == 'Program':
            for child in node.children:
                traverse_ast(child)

    traverse_ast(ast)
    return symbol_table

try:
    ast_parsed = parse(tokens)
    print("\n\n\nAnalizador Sintactico exitoso.")
    print_ast(ast_parsed)

    symbol_table = build_symbol_table(ast_parsed)
    

except SyntaxError as e:
    print("Syntax error:", str(e))
