import heapq

def prim(graph, start):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start)]  # (cost, node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        cost, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return total_cost

# Exemplo de grafo: lista de adjacência
grafo = [
    [(1, 2), (3, 6)],  # Nó 0
    [(0, 2), (2, 3), (3, 8), (4, 5)],  # Nó 1
    [(1, 3), (4, 7)],  # Nó 2
    [(0, 6), (1, 8)],  # Nó 3
    [(1, 5), (2, 7)]   # Nó 4
]

# Executando Prim a partir do nó 0
custo_total = prim(grafo, 0)
print(f"Custo total da árvore geradora mínima: {custo_total}")