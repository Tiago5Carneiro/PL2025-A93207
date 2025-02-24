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
```
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

### Output


## Lista de Resultados

- [tpc3.py](tpc3.py)
