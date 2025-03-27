# Recursivo Descendente para expressões aritméticas

## Autor
- Nome : Tiago André Leça Carneiro
- Número : A93207

<img src = "../media/722ff411-84c8-44a3-b34d-b639022e9b0e.jpg" alt = "eu" style="text-align = center;" width = "200">

## Resumo

Criar um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.

### Requisitos

Para sermos capazes de criar o parser, é necessário começar por criar um tokenizer capaz criar os seguintes tipos de tokens : 

```py
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
]
```
Após os tokens estarem definidos, foram definidas as precedências :

```py
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)
```

Por fim, foram criadas as expressões para o parser, seguindo as seguinte logica :

```
P1 : Expr -> Term Expr2

P2 : Expr2 --> '+' Term Expr2
P3 :         | '-' Term Expr2
P4 :         | ε

P5 : Term --> Factor Term2

P6 : Term2 --> '*' Factor Term2
P7 :         | '/' Factor Term2
P8 :         | ε

P9 : Factor --> '(' Expr ')'
P10:          | NUMBER
P11:          | '-' Factor
```

Resultando nas seguintes funções:

#### Função Expr  
```py
# P1
def rec_expr():
    value = rec_term()
    value = rec_expr2(value)
    return value 
```

#### Função Expr2 : 
```py
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
```

#### Função Term :
```py
# P5
def rec_term():
    value = rec_factor()
    value = rec_term2(value)
    return value
```


#### Função Term2 : 
```py
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
```
#### Função Factor :
```py
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
```

Por fim, a função inicial nesta extrutura recursiva é a função calculator.

#### Função Calculator : 
```py
def calculator(expression):
    global next_symbol
    lexer.input(expression)
    next_symbol = lexer.token()
    result = rec_expr()
    print(result)
    if next_symbol is not None:
        rec_error(next_symbol)
    return result
```

### Output

Testando com os inputs dados : 

<img src = "image.png" alt = "output" style="text-align = center;" width = "300">

## Lista de Resultados

- [tpc6.py](tpc6.py)
