# GRAFO ORIENTADO
# Grafo Orientado
# Matriz de Adjacência e Lista de Adjacência

n = int(input("Digite o número de vértices: "))
# Criar matriz
matriz = []
for i in range(n):
    matriz.append([0] * n)
# Criar lista de adjacência
lista = []

for i in range(n):
    lista.append([])

# Conjunto para controlar arestas repetidas
arestas_cadastradas = set()
quantidade = int(input("Digite o número de arestas: "))
contador = 0
while contador < quantidade:

    print(f"\nAresta", contador + 1)
    origem = int(input("Vértice de origem: "))
    destino = int(input("Vértice de destino: "))
    # Validar vértices
    if origem < 1 or origem > n or destino < 1 or destino > n:
        print("ERRO: vértice inválido!")
        print("Digite vértices entre 1 e", n)
        continue
    # Não permitir laços
    if origem == destino:
        print("ERRO: não é permitido ligar um vértice a ele mesmo!")
        continue
    # No grafo orientado a ordem importa
    aresta = (origem, destino)
    # Verificar repetição
    if aresta in arestas_cadastradas:
        print("ERRO: esta aresta já foi cadastrada!")
        continue
    arestas_cadastradas.add(aresta)

    # Matriz de adjacência
    matriz[origem - 1][destino - 1] = 1
    # Lista de adjacência
    lista[origem - 1].append(destino)
    contador += 1

# Mostrar matriz
print("\nMATRIZ DE ADJACÊNCIA")
for linha in matriz:
    print(linha)

# Mostrar lista
print("\nLISTA DE ADJACÊNCIA")
for i in range(n):
    print(i + 1, "->", lista[i])