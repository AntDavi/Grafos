import time  # Importa o módulo para medir o tempo

# Funções auxiliares para o Union-Find (ou DSU)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph, num_nodes):
    edges = []
    
    # Constrói uma lista de arestas do grafo
    for u in range(len(graph)):
        for v, weight in graph[u]:
            edges.append((weight, u, v))

    # Ordena as arestas pelo peso
    edges.sort()

    uf = UnionFind(num_nodes)
    mst_cost = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight
            mst_edges.append((u, v, weight))

    return mst_cost, mst_edges

# Exemplo de grafo: lista de adjacência
grafo = [
    [(1, 2), (3, 6)],  # Nó 0
    [(0, 2), (2, 3), (3, 8), (4, 5)],  # Nó 1
    [(1, 3), (4, 7)],  # Nó 2
    [(0, 6), (1, 8)],  # Nó 3
    [(1, 5), (2, 7)]   # Nó 4
]

# Medindo o tempo de execução
inicio = time.time()  # Marca o início
custo_total, mst = kruskal(grafo, len(grafo))
fim = time.time()  # Marca o fim

# Resultados
print(f"Custo total da árvore geradora mínima: {custo_total}")
print(f"Arestas da AGM: {mst}")
print(f"Tempo de execução: {fim - inicio:.6f} segundos")