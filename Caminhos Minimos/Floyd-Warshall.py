import time

class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = list(graph.keys())
        self.num_vertices = len(self.vertices)

    def find_all_pairs_shortest_path(self):
        # Inicializando a matriz de distâncias
        dist = {i: {j: float('inf') for j in self.vertices} for i in self.vertices}
        for u in self.graph:
            dist[u][u] = 0  # Distância de um nó para si mesmo é 0
            for v in self.graph[u]:
                dist[u][v] = self.graph[u][v]  # Distância direta

        # Aplicando o algoritmo de Floyd-Warshall
        for k in self.vertices:
            for i in self.vertices:
                for j in self.vertices:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Verificando ciclos negativos
        for v in self.vertices:
            if dist[v][v] < 0:
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

# Inicializando o algoritmo de Floyd-Warshall
fw = FloydWarshall(graph)

# Medindo o tempo de execução
start_time = time.time()
result = fw.find_all_pairs_shortest_path()
end_time = time.time()

# Exibindo o resultado
if result:
    print("Menor distância entre todos os pares de vértices:")
    for u in result:
        for v in result[u]:
            print(f"Distância de {u} para {v}: {result[u][v]}")
    print(f"\nTempo de execução: {end_time - start_time:.6f} segundos")
