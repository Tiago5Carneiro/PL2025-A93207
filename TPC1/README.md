# Somador (ON/OFF)

## Autor
- Nome : Tiago André Leça Carneiro
- Número : A93207

![eu](../media/722ff411-84c8-44a3-b34d-b639022e9b0e.jpg)

## Requisitos
Neste primeiro TPC foi nos pedido que criassemos um somador com os seguintes requesitos 

1. Some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse
comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse
comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída;
5. No fim, coloca o valor da soma na saída.

## Lista de Resultados

Foi nos providenciado o seguinte texto para teste:
```
"Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=OfF E deu-nos 7= dias para o fazer...ON Cada trabalho destes vale 0.25 valores da nota final!"
```

Compilando o programa utilizando o comando :

```sh
python3 TP1/tpc1.py
```

Observamos que, utilizando o teste fornecido, o resultado foi :

```sh
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=
>>2032
OfF
 E deu-nos 7=
>>2032
 dias para o fazer...ON
>>2057
```

## Solução

- [tpc1.py](tpc1.py)