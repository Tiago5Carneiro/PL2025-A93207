# Somador (ON/OFF)

Neste primeiro TPC foi nos pedido que criassemos um somador com os seguintes requesitos 

1. Some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse
comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse
comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída;
5. No fim, coloca o valor da soma na saída.

Foi nos providênciado o seguinte texto para teste:
```
"Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=OfF E deu-nos 7= dias para o fazer...ON Cada trabalho destes vale 0.25 valores da nota final!"
```

A solução presente no ficheiro tpc1.py, utilizando o teste dado pelos professores, foi capaz de apresentar a seguinte solução:

```
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=
>>2032
OfF
 E deu-nos 7=
>>2032
 dias para o fazer...ON
>>2057
```