import re
import ply.lex as lex

# Reserved words
reserved = {
    'select': 'SELECT',
    'where': 'WHERE',
    'limit': 'LIMIT'
}

# List of token names
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'DOT',
    'COLON',
    'EQUALS',
    'QMARK',
    'LBRACE',
    'RBRACE',
    'AT'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_DOT = r'\.'
t_COLON = r'\:'
t_EQUALS = r'='
t_QMARK = r'\?'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_AT = r'@'

# 
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Define a rule so we can track line numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r"\"[^']*\""
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

# Build the lexer
lexer = lex.lex()

# Test it out
data = open('input/test.file').read()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
