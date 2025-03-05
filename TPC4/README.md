# Analizador léxico

## Autor
- Nome : Tiago André Leça Carneiro
- Número : A93207

<img src = "../media/722ff411-84c8-44a3-b34d-b639022e9b0e.jpg" alt = "eu" style="text-align = center;" width = "200">

## Resumo

Construir um analisador léxico para uma liguagem de query.

### Requisitos

Ser capaz de analizar o seguinte tipo de mensagens :

```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Output

Ao analizar o exemplo, os seguintes tokens são identificados : 

<img src = "image.png" alt = "output" style="text-align = center;" width = "300">

## Lista de Resultados

- [tpc4.py](tpc4.py)
