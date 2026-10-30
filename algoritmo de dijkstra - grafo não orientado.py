import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]
    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))
    return distancias

grafo = {}
qtd_vertices = int(input("Digite a quantidade de vértices: "))
for i in range(qtd_vertices):
    vertice = input(f"Nome do vértice {i + 1}: ")
    grafo[vertice] = []
qtd_arestas = int(input("Digite a quantidade de arestas: "))
for i in range(qtd_arestas):
    origem =input("Origem: ")
    destino = input("Destino: ")
    peso = int(input("Peso da aresta: "))
    grafo[origem].append((destino, peso))
    grafo[destino].append((origem, peso))
    
inicio = input("Digite o vértice inicial: ")
resultado = dijkstra(grafo, inicio)
print("\nMenores distâncias:")
for vertice, distancia in resultado.items():
    print(f"{inicio} -> {vertice} = {distancia}")