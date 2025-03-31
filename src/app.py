import ply.lex as lex

tokens = (
    'IF', 'ELSE', 'WHILE', 'IDENTIFICADOR', 'NUMERO', 'NUMERO_FLOAT',
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'ASIGNACION', 'IGUALDAD',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'CORCHETE_IZQ', 'CORCHETE_DER', 'LLAVE_IZQ', 'LLAVE_DER',
    'DOS_PUNTOS', 'CADENA'
)

reservadas = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE',
}

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_IGUALDAD = r'=='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_DOS_PUNTOS = r':'

def t_CADENA(token):
    r'"([^\"]|\.)*"'
    token.value = token.value[1:-1]  # Remover comillas
    return token

def t_NUMERO_FLOAT(token):
    r'\d+\.\d+'
    token.value = float(token.value)
    return token

def t_NUMERO(token):
    r'\d+'
    token.value = int(token.value)
    return token

def t_IDENTIFICADOR(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'IDENTIFICADOR')
    return token

def t_COMENTARIO(token):
    r'\#.*'
    pass  # Ignorar comentarios

t_ignore = ' \t\n'

def t_error(token):
    print(f"Error léxico: Carácter ilegal '{token.value[0]}' en línea {token.lineno}")
    token.lexer.skip(1)

lexer = lex.lex()

codigo_ejemplo = """
if x == 10:
    y = x + 5.5 * 2
    mensaje = "Hola mundo"
    lista = [1, 2, 3]
    diccionario = {"clave": "valor"}
    # Esto es un comentario
else:
    y = x - 2 / 4
"""

lexer.input(codigo_ejemplo)

print("\nTokens generados:")
print("{:<15} {:<15} {:<10}".format("Token", "Valor", "Línea"))
print("-" * 40)
for token in lexer:
    print("{:<15} {:<15} {:<10}".format(token.type, str(token.value), token.lineno))

print("\nPrueba interactiva (escribe 'salir' para terminar):")
while True:
    try:
        entrada = input(">> ")
        if entrada.lower() == 'salir':
            break
        lexer.input(entrada)
        for tok in lexer:
            print(tok.type, tok.value)
    except Exception as e:
        print("Error:", e)
