#  Sabor Express - Rota Inteligente

##  Descrição do Projeto

O projeto Sabor Express - Rota Inteligente foi desenvolvido para uma empresa fictícia de delivery de alimentos que enfrenta dificuldades no gerenciamento das entregas durante os horários de maior demanda.

O objetivo é utilizar conceitos de Inteligência Artificial e algoritmos de busca para auxiliar na organização das entregas, buscando reduzir deslocamentos desnecessários e melhorar a eficiência das rotas.

A cidade é representada por meio de um grafo, no qual os pontos representam locais da cidade e as ruas são representadas por arestas com pesos relacionados às distâncias.

Além disso, o projeto utiliza o algoritmo K-Means para agrupar pedidos que possuem localização próxima, criando grupos de entregas que podem ser atendidos de maneira mais organizada.

---

##  Objetivos

Os principais objetivos do projeto são:

- Representar uma região da cidade utilizando um grafo;
- Representar ruas e suas respectivas distâncias;
- Utilizar o algoritmo A* para encontrar caminhos entre pontos;
- Utilizar o algoritmo K-Means para agrupar pedidos próximos;
- Organizar os pedidos dentro de cada grupo;
- Calcular a distância percorrida em cada rota;
- Gerar gráficos para visualizar os agrupamentos;
- Avaliar os resultados obtidos e identificar limitações da solução.

---

##  Abordagem da Solução

A solução foi dividida em etapas.

### 1. Representação do grafo

Foram definidos cinco pontos da cidade:

- A
- B
- C
- D
- E

As ruas foram representadas por meio de um dicionário contendo os pontos vizinhos e suas respectivas distâncias.

Exemplo:

```python
ruas = {
    "A": {"B": 4, "D": 3},
    "B": {"A": 4, "C": 2},
    "C": {"B": 2, "D": 2, "E": 3},
    "D": {"A": 3, "C": 2, "E": 1},
    "E": {"C": 3, "D": 1}
}