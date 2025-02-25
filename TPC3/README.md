# Análise de um dataset de obras musicais 

## Autor
- Nome : Tiago André Leça Carneiro
- Número : A93207

<img src = "../media/722ff411-84c8-44a3-b34d-b639022e9b0e.jpg" alt = "eu" style="text-align = center;" width = "200">

## Resumo
### Requisitos

Neste TPC foi pedido que gerassemos um ficheiro HTML a partir de um ficheiro Markdown com a seguinte sintaxe básica:

1. Cabeçalhos `# Exemplo`;
2. Bold `**exemplo**`;
3. Itálico `*exemplo*`;
4. Lista númerada : 
```md
1. um
2. dois
3. tres
```
5. Link `[texto](endereço)`;
6. Imagem `![texto alternativo](path para a imagem)`

### Solução

Para esta solução, houve duas ideologias que utilizei para alcançar o objetivo.

Para o Bold,Itálico,Imagens e Links, decidi utilizar a função re.sub e as seguintes expressões :
- Bold : `(.*?)\*\*(.*?)\*\*(.*?)`
- Itálico : `(.*?)\*(.*?)\*(.*?)`
- Imagens : `(.*?)!\[(.*?)\]\((.*?)\)(.*?)`
- Link : `(.*?)\[(.*?)\]\((.*?)\)(.*?)`

Para os Headers e as Listas, decidi seguir uma estrutura diferente:
- Para os Headers, utilizo a expressão ` *#` num split, para perceber se primeiro, a linha começa por um espaço ou um '#', e para também fácilmente contar a quantidade de '#' que existem, pois é só contar a quantidade de strings vazias seguidas após o split ser realizado.
- Para as listas, utilando a expressão `^[1-9]+\.` verifico se a linha começa com a estrutura necessária para uma lista, se sim e se a váriavel `was_list` for falsa, então sabemos que é o primeiro elemento da lista, e colocamos esta variável a verdadeiro. Para fechar a lista, assim que uma linha não tiver esta estrutura, mas a váriavel se encontrar a verdadeira, fechamos a lista, e colocamos a variável de volta a falso. Esta verificação para fechar a lista é também feita no final do ficheiro.

Um pequeno detalhe adicionado foi o facto de que, quando uma lista for criada, caso apareça novamente o número 1, optei por fechar a lista atual e começar uma nova.

### Output

#### Input file

```md
###### *Title*

*Hello* **world** **101**.

This is my first file!

1. *ola*
2. **mundo**
1. ahhhhh

This is a [photo](www.google.pt) of my ![cat](../media/cat.jpg) and [photo2](www.google.pt) and ![cat](../media/cat.jpg)
```

#### Output File

```html
<h6><i>Title</i></h6>

<i>Hello</i> <b>world</b> <b>101</b>.

This is my first file!

<ol>
<li><i>ola</i></li>
<li><b>mundo</b></li>
</ol>
<ol>
<li>ahhhhh</li>
</ol>

This is a <a href="www.google.pt">photo</a> of my <img src="../media/cat.jpg" alt="cat"> and <a href="www.google.pt">photo2</a> and <img src="../media/cat.jpg" alt="cat">
```
## Lista de Resultados

- [tpc3.py](tpc3.py)
