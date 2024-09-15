import heapq
import time

def dijkstra(graph, start):
    # Inicializar a distância de todos os vértices como infinito e a origem com 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Fila de prioridade para processar o vértice com a menor distância conhecida
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Se a distância processada for maior que a distância armazenada, continue
        if current_distance > distances[current_vertex]:
            continue

        # Processar todos os vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Se for encontrado um caminho mais curto para o vizinho
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def measure_dijkstra_time(graph, start):
    start_time = time.time()  # Iniciar a medição de tempo
    distances = dijkstra(graph, start)  # Executar o algoritmo de Dijkstra
    end_time = time.time()  # Parar a medição de tempo
    execution_time = end_time - start_time  # Calcular o tempo de execução

    # Exibir o resultado
    print("Menor distância de '{}' para os outros vértices:".format(start))
    for vertex in distances:
        print(f"Distância até {vertex}: {distances[vertex]}")

    print(f"\nTempo de execução: {execution_time:.6f} segundos")

# Exemplo de entrada
graph = {
    'A': {'B': 3, 'C': 6},
    'B': {'A': 3, 'C': 4, 'D': 4},
    'C': {'A': 6, 'B': 4, 'D': 8, 'E': 3},
    'D': {'B': 4, 'C': 8, 'E': 2, 'F': 5},
    'E': {'C': 3, 'D': 2, 'F': 3},
    'F': {'D': 5, 'E': 3}
}

# Executando o algoritmo de Dijkstra e medindo o tempo de resposta
start_vertex = 'A'
measure_dijkstra_time(graph, start_vertex)
