# Lista de Tokens
tokens = ('IDENTIFICADOR','NUMERO','SUMA','RESTA','MULTIPLICACION','DIVISION',
          'ASIGNACION','MENOR','MENORQUE','MAYOR','MAYORQUE',
          'PARENTESIS_IZQ','PARENTESIS_DER','COMA','PUNTO_Y_COMA','PUNTO',
          'LLAVE_IZQ','LLAVE_DER' 
)

# Palabras Reservadas
reservadas = (
    'SI',
    'SINO',
    'MIENTRAS',
    'DO',
    'ENTERO',
    'PARA',
    'IN'
)

tokens = tokens+reservadas

# Expresiones Regulares para tokens Simples

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r':='
t_MENOR = r'<'
t_MENORQUE = r'<='
t_MAYOR = r'>'
t_MAYORQUE = r'>='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_PUNTO = r'\.'
t_LLAVE_IZQ = r'\['
t_LLAVE_DER = r'\]'

def t_SI(t):
    r'if'
    return t
# Expresion Regular para Cualquier cantidad de letras de variable
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in tokens:
        t.type = t.value.upper()
    return t

# para que acepte comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

# Expresion regular para cualquier cantidad de numeros enteros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newLine(t):
    # Define Saltos de Lineas
    r'\n+'
    t.lexer.lineno += len(t.value)

# Cadena de caracteres a ignorar (espacios, tabulaciones y saltos de linea)
t_ignore = ' \t'


def t_error(t):
    # Manejo de errores, si un caracter de entrada no coincide con los tokens
    # este metodo indica cual es ese caracter
    global respuesta_Parser
    resultado = "Caracter Invalido '%s'" % t.value[0]
    respuesta_Parser.append(resultado)
    t.lexer.skip(1)

# Instanciamos el Analizador Lexico.
import ply.lex as lex
lexer = lex.lex()