import time
from collections import deque

# Função auxiliar para realizar a busca por caminho aumentante (BFS)
def bfs(rGraph, source, sink, parent):
    visited = [False] * len(rGraph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in enumerate(rGraph[u]):
            if not visited[v] and capacity > 0:  # Aresta com capacidade residual
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

# Implementação do algoritmo de Ford-Fulkerson
def ford_fulkerson(graph, source, sink):
    rGraph = [row[:] for row in graph]  # Grafo residual (cópia do grafo original)
    parent = [-1] * len(graph)  # Array para armazenar o caminho aumentante
    max_flow = 0  # Fluxo máximo inicialmente

    while bfs(rGraph, source, sink, parent):
        # Encontra a capacidade mínima ao longo do caminho aumentante encontrado
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]

        # Atualiza as capacidades residuais das arestas
        v = sink
        while v != source:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

        # Adiciona o fluxo encontrado ao fluxo máximo total
        max_flow += path_flow

    return max_flow

# Exemplo de grafo
grafo = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

# Medindo o tempo de execução
inicio = time.time()  # Marca o início
fluxo_maximo = ford_fulkerson(grafo, fonte, sorvedouro)
fim = time.time()  # Marca o fim

# Resultados
print(f"Fluxo máximo: {fluxo_maximo}")
print(f"Tempo de execução: {fim - inicio:.6f} segundos")