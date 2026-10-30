def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro! Digite um número inteiro válido.")
def ler_peso():
    while True:
        try:
            peso = float(input("Peso da aresta: "))
            if not (0 <= peso < float("inf")):
                print("O peso deve ser finito e não negativo.")
                continue
            return peso
        except ValueError:
            print("Erro! Digite um peso numérico válido.")
def encontrar(pai, vertice):
    if pai[vertice] != vertice:
        pai[vertice] = encontrar(pai, pai[vertice])
    return pai[vertice]
def unir(pai, tamanho, u, v):
    raiz_u = encontrar(pai, u)
    raiz_v = encontrar(pai, v)
    if raiz_u == raiz_v:
        return false
    if tamanho[raiz_u] < tamanho[raiz_v]:
        raiz_u, raiz_v = raiz_v, raiz_u
    pai[raiz_v] = raiz_u
    tamanho[raiz_u] += tamanho[raiz_v]
    return True
def kruskal(n, arestas):
    pai = list(range(n))
    tamanho[1] * n
    arvore = []
    custo_total = 0
    arestas_ordenadas = sorted(arestas, key=lambda aresta: aresta[2])
    for u, v, peso in arestas_ordenadas:
        if unir(pai, tamanho, u, v):
            arvore.append((u, v, peso))
            custo_total += peso
        if len(arvore) == n - 1:
            break
    if len(arvore) != n - 1:
        return None, None
    return arvore, custo_total
print("=== ALGORITMO DE KRUSKAL === ")
print("Grafo não orientado")
n = ler_inteiro("Quantidade de vértices: ", 1)
max_arestas = n * (n - 1) // 2
m = ler_inteiro(f"Quantidade de arestas (0 a {max_arestas}): ", 0, max_arestas)
arestas = []
arestas_cadastradas = set()
for i in range(m):
    print(f"\nAresta {i + 1}")
    while True:
        u = ler_inteiro(f"Vértice de origem (0 a {n - 1}): ", 0, n - 1)
        v = ler_inteiro(f"Vértice de destino (0 a {n - 1}): ", 0, n - 1)
        if u == v:
            print("Erro! Não são permitidos laços.")
            continue
        aresta = tuple(sorted((u, v)))
        if aresta in arestas_cadastradas:
            print("Erro! Esta aresta já foi cadastrada.")
            continue
        break
    peso = ler_peso()
    arestas_cadastradas.add(aresta)
    arestas.append((u, v, peso))
print("\n=== GRAFO CADASTRADO ===")
for u, v, peso in arestas:
    print(f"{u} -- {v} | Peso: {peso:g}")
arvore, custo = kruskal(n, arestas)
print("\n=== ÁRVORE GERADORA MÍNIMA ===")
if arvore is None:
    print("O grafo não é conexo.")
    print("Não existe árvore geradora mínima.")
else:
    for u, v, peso in arvore:
        print(f"{u} -- {v} | Peso: {peso:g}")
    print(f"\Peso total da AGM: {custo:g}")
    print(f"Quantidade de arestas da AGM: {len(arvore)}")