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

# Precedence rules, unitary minus operator has higher precedence than the rest
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    if p[3] == 0:
        raise ZeroDivisionError("division by zero")
    p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_error(p):
    if p :
        print(f"Syntax error in token '{p.value}'")
    else:
        print("Syntax error at EOF")

def calculator(expression):
    try : 
        output = parser.parse(expression, lexer=lexer)
        return output
    except ZeroDivisionError as e:
        return f"Division by zero is not allowed in {e}"
    except Exception as e:
        return f"An error occurred in {e}"

def main():
    global lexer,parser
    lexer = lex.lex()
    parser = yacc.yacc()
    while True:
        print("Calculator (type 'exit' to leave)")
        command = input("calc: ")
        if command == "exit":
            break
        output = calculator(command)
        if output:
            print(f"calc: {output}")

if __name__ == "__main__":
    main()