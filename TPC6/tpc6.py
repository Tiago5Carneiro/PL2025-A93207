import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = r' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# P1 : Expr -> Term Expr2

# P2 : Expr2 --> '+' Term Expr2
# P3 :         | '-' Term Expr2
# P4 :         | ε

# P5 : Term --> Factor Term2

# P6 : Term2 --> '*' Factor Term2
# P7 :         | '/' Factor Term2
# P8 :         | ε

# P9 : Factor --> '(' Expr ')'
# P10:          | NUMBER
# P11:          | '-' Factor

next_symbol = ('Erro', '', 0, 0)

def rec(symbol):
    global next_symbol
    if next_symbol.type == symbol:
        value = next_symbol.value
        next_symbol = lexer.token()
        return value
    else:
        print(f"Syntax error: {symbol} expected")

def rec_error(symbol):
    print(f"Syntax error: unexpected symbol '{symbol.value}'")

# P1
def rec_expr():
    value = rec_term()
    value = rec_expr2(value)
    return value 

# P2, P3, P4
def rec_expr2(value):
    global next_symbol
    if next_symbol is not None :
        if next_symbol.type == 'PLUS':
            rec('PLUS')
            value2 = rec_term()
            return rec_expr2(value + value2)
        elif next_symbol.type == 'MINUS':
            rec('MINUS')
            value2 = rec_term()
            return rec_expr2(value - value2)
    return value

# P5
def rec_term():
    value = rec_factor()
    value = rec_term2(value)
    return value

# P6, P7, P8
def rec_term2(value):
    global next_symbol
    if next_symbol is not None:
        if next_symbol.type == 'TIMES':
            rec('TIMES')
            value2 = rec_factor()
            return rec_term2(value * value2)
        elif next_symbol.type == 'DIVIDE':
            rec('DIVIDE')
            value2 = rec_factor()
            return rec_term2(value / value2)
    return value

# P9, P10, P11
def rec_factor():
    global next_symbol
    if next_symbol is not None:
        if next_symbol.type == 'LPAREN':
            rec('LPAREN')
            value = rec_expr()
            rec('RPAREN')
            return value
        elif next_symbol.type == 'NUMBER':
            return int(rec('NUMBER'))
        elif next_symbol.type == 'MINUS':
            rec('MINUS')
            return -rec_factor()
    return 0

def calculator(expression):
    global next_symbol
    lexer.input(expression)
    next_symbol = lexer.token()
    result = rec_expr()
    print(result)
    if next_symbol is not None:
        rec_error(next_symbol)
    return result

def main():
    global lexer, next_symbol
    lexer = lex.lex()
    while True:
        print("Calculator (type 'exit' to leave)")
        command = input("calc: ")
        if command == "exit":
            break
        lexer.input(command)
        next_symbol = lexer.token()
        output = rec_expr()
        if output:
            print(f"calc: {output}")

if __name__ == "__main__":
    main()