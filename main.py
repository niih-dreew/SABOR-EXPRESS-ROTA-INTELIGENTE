# Pontos da cidade
pontos = ["A", "B", "C", "D", "E"]

# Ruas e suas distâncias
ruas = {
    "A": {"B": 4, "D": 3},
    "B": {"A": 4, "C": 2},
    "C": {"B": 2, "D": 2, "E": 3},
    "D": {"A": 3, "C": 2, "E": 1},
    "E": {"C": 3, "D": 1}
}

print("Pontos da cidade:")
print(pontos)

print("\nRuas:")
print(ruas)
# Testando uma rota
origem = "A"
destino = "D"

distancia = ruas[origem][destino]

print("\nTeste de rota:")
print(f"De {origem} para {destino}: {distancia} km")
# Coordenadas dos pontos no mapa
coordenadas = {
    "A": (0, 0),
    "B": (0, 4),
    "C": (3, 4),
    "D": (3, 1),
    "E": (4, 1)
}

print("\nCoordenadas:")
print(coordenadas)
import math


# Função que calcula a distância estimada entre dois pontos
def heuristica(ponto_atual, destino):
    x1, y1 = coordenadas[ponto_atual]
    x2, y2 = coordenadas[destino]

    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distancia


# Testando a heurística
estimativa = heuristica("D", "E")

print("\nHeurística:")
print(f"Distância estimada de D até E: {estimativa:.2f} km")
# Calculando o valor do A*
g = 3  # distância que já percorremos de A até D
h = heuristica("D", "E")  # distância estimada de D até E

f = g + h

print("\nCálculo do A*:")
print(f"Distância percorrida (g): {g} km")
print(f"Heurística (h): {h:.2f} km")
print(f"Valor total (f): {f:.2f} km")
# Algoritmo A*
def a_estrela(inicio, objetivo):
    abertos = [inicio]
    veio_de = {}

    custo = {inicio: 0}

    while abertos:

        atual = min(
            abertos,
            key=lambda ponto: custo[ponto] + heuristica(ponto, objetivo)
        )

        if atual == objetivo:
            caminho = [atual]

            while atual in veio_de:
                atual = veio_de[atual]
                caminho.append(atual)

            caminho.reverse()
            return caminho

        abertos.remove(atual)

        for vizinho, distancia in ruas[atual].items():

            novo_custo = custo[atual] + distancia

            if vizinho not in custo or novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                veio_de[vizinho] = atual

                if vizinho not in abertos:
                    abertos.append(vizinho)

    return None


# Testando o A*
# Testando o A*
rota = a_estrela("A", "E")

print("\n===== TESTE DO A* =====")

if rota:
    print("Menor caminho encontrado:")
    print(" → ".join(rota))
else:
    print("Nenhum caminho encontrado.")
# Pedidos da Sabor Express
pedidos = {
    "Pedido 1": (0, 0),
    "Pedido 2": (1, 1),
    "Pedido 3": (0, 2),
    "Pedido 4": (5, 5),
    "Pedido 5": (6, 5),
    "Pedido 6": (5, 6),
    "Pedido 7": (10, 1),
    "Pedido 8": (11, 1),
    "Pedido 9": (10, 2),
    "Pedido 10": (6, 2)
}

print("\nPedidos da Sabor Express:")

for pedido, coordenada in pedidos.items():
    print(f"{pedido}: {coordenada}")
    from sklearn.cluster import KMeans

# Transformando os pedidos em uma lista de coordenadas
coordenadas_pedidos = list(pedidos.values())

# Criando o K-Means com 3 grupos
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Fazendo o agrupamento
kmeans.fit(coordenadas_pedidos)

# Descobrindo o grupo de cada pedido
grupos = kmeans.labels_

print("\nGrupos encontrados pelo K-Means:")

for i, grupo in enumerate(grupos):
    print(f"{list(pedidos.keys())[i]} → Grupo {grupo + 1}")
    import matplotlib.pyplot as plt

# Criando o gráfico
for grupo in range(3):
    pontos_grupo = [
        coordenadas_pedidos[i]
        for i in range(len(coordenadas_pedidos))
        if grupos[i] == grupo
    ]

    x = [ponto[0] for ponto in pontos_grupo]
    y = [ponto[1] for ponto in pontos_grupo]

    plt.scatter(x, y, label=f"Grupo {grupo + 1}")

# Colocando o nome de cada pedido no gráfico
for i, (pedido, coordenada) in enumerate(pedidos.items()):
    x, y = coordenada
    plt.text(x + 0.1, y + 0.1, pedido, fontsize=8)

# Nome dos eixos
plt.xlabel("Posição X")
plt.ylabel("Posição Y")

# Título
plt.title("Agrupamento de Entregas - Sabor Express")

# Legenda
plt.legend()

# Grade
plt.grid(True)

# Mostrar o gráfico


# Nome dos eixos
plt.xlabel("Posição X")
plt.ylabel("Posição Y")

# Título
plt.title("Agrupamento de Entregas - Sabor Express")

# Mostrar legenda
plt.legend()

# Mostrar o gráfico
plt.savefig("outputs/graficos_kmeans.png")
plt.show()

# ==========================================
# CRIANDO AS ROTAS POR GRUPO
# ==========================================

print("\n===== ROTAS INTELIGENTES =====")

rotas = {}

for grupo in range(3):
    pedidos_grupo = []

    for i, grupo_pedido in enumerate(grupos):
        if grupo_pedido == grupo:
            pedidos_grupo.append(i)

    rotas[grupo] = pedidos_grupo

    print(f"\nRota do Grupo {grupo + 1}:")

    for i in pedidos_grupo:
        print(f"Pedido {i + 1}", end=" -> ")

    print("Fim")

    # ==========================================
# CALCULANDO A DISTÂNCIA ENTRE OS PEDIDOS
# ==========================================

def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2

    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distancia
# ==========================================
# ORGANIZANDO OS PEDIDOS PELA DISTÂNCIA
# ==========================================

# ==========================================
# ORGANIZANDO OS PEDIDOS PELA DISTÂNCIA
# ==========================================

for grupo, pedidos_grupo in rotas.items():

    if len(pedidos_grupo) > 1:

        inicio = pedidos_grupo[0]
        restantes = pedidos_grupo[1:]

        pedidos_ordenados = [inicio]

        while restantes:

            atual = pedidos_ordenados[-1]

            proximo = min(
                restantes,
                key=lambda i: calcular_distancia(
                    coordenadas_pedidos[atual],
                    coordenadas_pedidos[i]
                )
            )

            pedidos_ordenados.append(proximo)
            restantes.remove(proximo)

        rotas[grupo] = pedidos_ordenados

print("\n===== ROTAS ORGANIZADAS =====")

for grupo, pedidos_grupo in rotas.items():

    print(f"\nRota do Grupo {grupo + 1}:")

    for i in pedidos_grupo:
        print(f"Pedido {i + 1}", end=" -> ")

    print("Fim")
  # ==========================================
# DISTÂNCIA TOTAL DE CADA ROTA
# ==========================================

print("\n===== DISTÂNCIA DAS ROTAS =====")

for grupo, pedidos_grupo in rotas.items():

    distancia_total = 0

    for i in range(len(pedidos_grupo) - 1):
        pedido_atual = pedidos_grupo[i]
        proximo_pedido = pedidos_grupo[i + 1]

        distancia_total += calcular_distancia(
            coordenadas_pedidos[pedido_atual],
            coordenadas_pedidos[proximo_pedido]
        )

    print(
        f"Grupo {grupo + 1}: "
        f"{distancia_total:.2f} unidades de distância"
    )
# ==========================================
# DETALHANDO CADA ROTA
# ==========================================

print("\n===== DETALHAMENTO DAS ROTAS =====")

for grupo, pedidos_grupo in rotas.items():

    print(f"\nGrupo {grupo + 1}:")

    distancia_total = 0

    for i in range(len(pedidos_grupo)):

        pedido_atual = pedidos_grupo[i]
        nome_pedido = list(pedidos.keys())[pedido_atual]

        print(f"  {nome_pedido}: {pedidos[nome_pedido]}")

        if i < len(pedidos_grupo) - 1:

            proximo_pedido = pedidos_grupo[i + 1]

            distancia = calcular_distancia(
                pedidos[nome_pedido],
                pedidos[list(pedidos.keys())[proximo_pedido]]
            )

            distancia_total += distancia

            print(f"    ↓ {distancia:.2f} unidades")

    print(f"  Distância total: {distancia_total:.2f} unidades")
    print("Fim")

# ==========================================
# DISTÂNCIA TOTAL DE CADA ROTA
# ==========================================

print("\n===== DISTÂNCIA DAS ROTAS =====")

for grupo, pedidos_grupo in rotas.items():

    distancia_total = 0

    for i in range(len(pedidos_grupo) - 1):
        pedido_atual = pedidos_grupo[i]
        proximo_pedido = pedidos_grupo[i + 1]

        distancia_total += calcular_distancia(
            coordenadas_pedidos[pedido_atual],
            coordenadas_pedidos[proximo_pedido]
        )

    print(f"Grupo {grupo + 1}: {distancia_total:.2f} unidades")
    print("Fim")
    # ==========================================
# CALCULANDO A DISTÂNCIA TOTAL DAS ROTAS
# ==========================================

print("\n===== DISTÂNCIA DAS ROTAS =====")

for grupo, pedidos_grupo in rotas.items():

    distancia_total = 0

    for i in range(len(pedidos_grupo) - 1):

        pedido_atual = pedidos_grupo[i]
        proximo_pedido = pedidos_grupo[i + 1]

        distancia = calcular_distancia(
            coordenadas_pedidos[pedido_atual],
            coordenadas_pedidos[proximo_pedido]
        )

        distancia_total += distancia

    print(
        f"Grupo {grupo + 1}: "
        f"{distancia_total:.2f} km"
    )
print("Fim")
# ==========================================
# CALCULANDO A DISTÂNCIA TOTAL DAS ROTAS
# ==========================================

print("\n===== DISTÂNCIA DAS ROTAS =====")

for grupo, pedidos_grupo in rotas.items():

    distancia_total = 0

    for i in range(len(pedidos_grupo) - 1):

        pedido_atual = pedidos_grupo[i]
        proximo_pedido = pedidos_grupo[i + 1]

        distancia = calcular_distancia(
            coordenadas_pedidos[pedido_atual],
            coordenadas_pedidos[proximo_pedido]
        )

        distancia_total += distancia

    print(f"Grupo {grupo + 1}: {distancia_total:.2f} km")

print("Fim")
# ==========================================
# GERANDO DIAGRAMA DO GRAFO
# ==========================================

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

# Desenhando as ruas
for origem, vizinhos in ruas.items():
    for destino, distancia in vizinhos.items():

        x1, y1 = coordenadas[origem]
        x2, y2 = coordenadas[destino]

        plt.plot(
            [x1, x2],
            [y1, y2],
            linewidth=2
        )

        # Mostra a distância da rua
        meio_x = (x1 + x2) / 2
        meio_y = (y1 + y2) / 2

        plt.text(
            meio_x,
            meio_y,
            f"{distancia} km",
            fontsize=9
        )

# Desenhando os pontos
for ponto, (x, y) in coordenadas.items():

    plt.scatter(x, y, s=150)

    plt.text(
        x + 0.1,
        y + 0.1,
        ponto,
        fontsize=12,
        fontweight="bold"
    )

plt.title("Grafo de Rotas - Sabor Express")
plt.xlabel("Posição X")
plt.ylabel("Posição Y")
plt.grid(True)

plt.savefig("docs/grafo.png")
plt.show()
