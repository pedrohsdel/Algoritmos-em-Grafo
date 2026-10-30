# Grafo não orientado
# Matriz de Adjacência e Lista de Adjacência
# Com validação das arestas

n = int(input("Digite o número de vértices: "))
# Criar matriz de adjacência
matriz = []
for i in range(n):
    matriz.append([0] * n)
# Criar lista de adjacência
lista = []
for i in range(n):
    lista.append([])
# Conjunto para guardar as arestas já cadastradas
arestas_cadastradas = set()
quantidade = int(input("Digite o número de arestas: "))
contador = 0
while contador < quantidade:
    print(f"\nAresta", contador + 1)
    origem = int(input("Vértice de origem: "))
    destino = int(input("Vértice de destino: "))
    # Validar vértices fora do intervalo
    if origem < 1 or origem > n or destino < 1 or destino > n:
        print("ERRO: vértice inválido!")
        print("Digite vértices entre 1 e", n)
        continue

    # Evitar ligação do vértice com ele mesmo
    if origem == destino:
        print("ERRO: não é permitido ligar um vértice a ele mesmo!")
        continue
    # Padronizar a aresta
    if origem < destino:
        aresta = (origem, destino)
    else:
        aresta = (destino, origem)
    # Verificar se a aresta já existe
    if aresta in arestas_cadastradas:
        print("ERRO: esta aresta já foi cadastrada!")
        continue
    # Guardar aresta
    arestas_cadastradas.add(aresta)

    # Preencher matriz
    matriz[origem - 1][destino - 1] = 1
    matriz[destino - 1][origem - 1] = 1
    # Preencher lista
    lista[origem - 1].append(destino)
    lista[destino - 1].append(origem)

    contador += 1

# Mostrar matriz de adjacência
print("\nMATRIZ DE ADJACÊNCIA")
for linha in matriz:
    print(linha)

# Mostrar lista de adjacência
print("\nLISTA DE ADJACÊNCIA")

for i in range(n):
    print(i + 1, "->", lista[i])