import re

# Definir los patrones de los tokens utilizando expresiones regulares
token_patterns = [
    (r'int', 'INT'),
    (r'print', 'PRINT'),               # Imprimir
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Variables
    (r'=', 'ASSIGN'),                  # Asignación
    (r'\d+', 'NUMBER'),                # Número entero
    (r'\+', 'PLUS'),                   # Suma
    (r';', 'SEMICOLON'),               # Punto y coma
    (r'\(', 'LPAREN'),                  # Paréntesis izquierdo
    (r'\)', 'RPAREN'),                  # Paréntesis derecho
]


# Función para analizar la cadena de entrada y generar los tokens
def lexer(input_string):
    tokens = []
    position = 0

    while position < len(input_string):
        match = None

        # Buscar el patrón coincidente más largo en la posición actual
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_string, position)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((value, token_type))
                position = match.end(0)
                break

        # Si no se encontró ninguna coincidencia, se omite el carácter actual
        if not match:
            position += 1

    return tokens

# Ejemplo de uso
input_string = '''
    int a = 5;
    int b = 10;
    int c = a + b;
    print(c);
'''
tokens = lexer(input_string)
print('\n\nTokens:')
# Imprimir los tokens generados
for token in tokens:
    print(token)



