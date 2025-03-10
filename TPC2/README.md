# Análise de um dataset de obras musicais 

## Autor
- Nome : Tiago André Leça Carneiro
- Número : A93207

<img src = "../media/722ff411-84c8-44a3-b34d-b639022e9b0e.jpg" alt = "eu" style="text-align = center;" width = "200">

## Resumo
### Requisitos

Neste TPC foi pedido que fosse analizado um ficherio CSV e que, sem utilizar o módulo CSV do python fosse possível apresentar:

1. Lista ordenada alfabeticamente dos compositores musicais;
2. Distribuição das obras por período: quantas obras catalogadas em cada período;
3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

### Solução

Para a resolução deste TPC foi necessário pensar numa expressão regular capaz de capturar todas as entradas presentes no [CSV](obras.csv). Após pensar um pouco sobre o problema, cheguei a seguinte expressão:

---
**EXPRESSION**

<!---
^<span id="name" style="color:cornflowerblue">([^;]+);</span><span id="description" style="color:lightpink">("(?:[^"]|"")* "|[^;]* );</span><span id="creationyear" style="color:violet">(\d{4});</span><span id="period" style="color:green">([^;]+);</span><span id="composer" style="color:firebrick">([^;]+);</span><span id="duration" style="color:orange">(\d{2}:\d{2}:\d{2});</span><span id="id" style="color:coral">(O\d+)</span>$
-->

```
^([^;]+);("(?:[^"]|"")*"|[^;]*);(\d{4});([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});(O\d+)$
```

---

Primeiramente, para conseguirmos compreender esta expressão, temos que considerar que os dados seguem a seguinte estrutura :
```
nome;desc;anoCriacao;periodo;compositor;duracao;_id
```
A primeira coisa que podemos reparar é o facto de que cada grupo é separado pelo caracter ';' . Assim, na expressão anterior obrigamos a que o caracter ';' apareça entre cada grupo.

Com isto em mente, podemos agora falar de cada grupo em específico:

- <span id="name" style="color:cornflowerblue">Nome - </span> ```([^;]+);``` Começamos por dar match no primeiro grupo a todos os caracteres expecto pelo ';', já que sabemos que esse vai apenas aparecer no fim.
- <span id="description" style="color:lightpink">Descrição - </span> ```("(?:[^"]|"")* "|[^;]* );``` Aqui procuramos por texto que esteja entre aspas (" "), tendo em conta que este campo pode estar vazio, e ignorando aspas extras que possam ser encontradas pelo meio da descrição. Algo igualmente importante é o facto de que o grupo interno que ignora as aspas que possam existir já entre aspas é non-capturing, para que cada grupo capturado expresse a estrutura anteriormente mencionada
- <span id="creationyear" style="color:violet">Ano de Criação - </span>```(\d{4});``` Para o ano de criação, procuramos por 4 dígitos seguidos de ';' .
- <span id="period" style="color:green">Período - </span>```([^;]+);``` Procuramos todos os elementos excepto ';', mas acabando com esse caracter.
- <span id="composer" style="color:firebrick">Compositor - </span>```([^;]+);``` Exatamente o mesmo processo que para o campo anterior.
- <span id="duration" style="color:orange">Duração - </span> ```(\d{2}:\d{2}:\d{2});``` Para a duração, procuramos pela estrutura comum para representar um espaço de tempo, 2 dígitos para as horas, seguidos por ':', 2 dígitos para os minutos, seguidos por ':', e por fim 2 dígitos para os segundos.
- <span id="id" style="color:coral">ID - </span>```(O\d+)``` para o id, começamos por procurar pela letra O seguida de dígitos, já que esta é a estrutura dos id's presentes no [CSV](obras.csv) .

Após serem encontradas as respetivas correspondências para a expressão regular mencionada acima, são criadas as seguintes estruturas de dados:

- <span style="color:teal">Composers - </span>Um *Set* onde ficaram guardados os nomes dos compositores presentes no [CSV](obras.csv), sendo este *Set* ordenado alfabéticamente após a leitura na totalidade do mesmo.
- <span style="color:gold">Period_Count - </span> Um dicionário onde a chave é o período da obra, e o valor é a sua frequência.
- <span style="color:yellowgreen">Period_Works - </span> Um dicionário onde a chave é o período da obra, e o valor é uma lista dos nomes das obras com esse período, ordenada alfabéticamente.

Para além do ficheiro com a solução ([tpc2.py](tpc2.py)) adicionei o ficheiro [pagination.py](pagination.py), com funções para poder representar sets e dicionários de uma forma paginada, para melhor clareza e leitura.

### Output
#### Menu
<img src = "image-1.png" alt = "eu" style="text-align = center;" width = "200">

#### 1.

<img src = "image.png" alt = "eu" style="text-align = center;" width = "500">

#### 2.

<img src = "image-2.png" alt = "eu" style="text-align = center;" width = "500">

#### 3.
![alt text](image-3.png)
## Lista de Resultados

- [tpc2.py](tpc2.py)
- [pagination.py](pagination.py)
