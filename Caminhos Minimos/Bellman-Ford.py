import time

class BellmanFord:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = list(graph.keys())

    def find_shortest_path(self, start):
        dist = {vertex: float('inf') for vertex in self.vertices}
        dist[start] = 0
        predecessor = {vertex: None for vertex in self.vertices}

        # Relaxamento das arestas |V| - 1 vezes
        for _ in range(len(self.vertices) - 1):
            for u in self.graph:
                for v, weight in self.graph[u].items():
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        predecessor[v] = u

        # Verifica ciclos negativos
        for u in self.graph:
            for v, weight in self.graph[u].items():
                if dist[u] + weight < dist[v]:
                    print("Grafo contém ciclo de peso negativo")
                    return None

        return dist

# Exemplo de uso:
graph = {
    'A': {'B': 3, 'C': 6},
    'B': {'A': 3, 'C': 4, 'D': 4},
    'C': {'A': 6, 'B': 4, 'D': 8, 'E': 3},
    'D': {'B': 4, 'C': 8, 'E': 2, 'F': 5},
    'E': {'C': 3, 'D': 2, 'F': 3},
    'F': {'D': 5, 'E': 3}
}

# Inicializando o algoritmo de Bellman-Ford
bf = BellmanFord(graph)

# Medindo o tempo de execução
start_time = time.time()
result = bf.find_shortest_path('A')
end_time = time.time()

# Exibindo o resultado
if result:
    print("Menor distância de 'A' para os outros vértices:")
    for vertex in result:
        print(f"Distância até {vertex}: {result[vertex]}")
    print(f"\nTempo de execução: {end_time - start_time:.6f} segundos")