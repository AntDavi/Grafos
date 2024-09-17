import time

# Função para realizar a coloração gulosa de um grafo
def coloracao_gulosa(grafo):
    n = len(grafo)  # Número de vértices
    resultado = [-1] * n  # Inicialmente nenhum vértice está colorido (-1 significa não colorido)
    
    # Atribuindo a primeira cor ao primeiro vértice
    resultado[0] = 0
    
    # Armazena as cores disponíveis para os vértices adjacentes
    cores_disponiveis = [False] * n
    
    # Processa os demais vértices
    for u in range(1, n):
        # Marca como indisponível as cores dos vértices adjacentes
        for i in grafo[u]:
            if resultado[i] != -1:
                cores_disponiveis[resultado[i]] = True
        
        # Encontra a primeira cor disponível
        cor = 0
        while cor < n and cores_disponiveis[cor]:
            cor += 1
        
        # Atribui a menor cor disponível ao vértice atual
        resultado[u] = cor
        
        # Reseta a lista de cores disponíveis para a próxima iteração
        for i in grafo[u]:
            if resultado[i] != -1:
                cores_disponiveis[resultado[i]] = False
    
    return resultado

# Função principal para medir o tempo de execução
def executar_coloracao_com_tempo(grafo):
    inicio = time.time()
    resultado = coloracao_gulosa(grafo)
    fim = time.time()
    return resultado, fim - inicio

# Exemplo de grafo
grafo = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# Executando a coloração
resultado, tempo_execucao = executar_coloracao_com_tempo(grafo)

# Exibindo o resultado da coloração
print(f"Coloração dos vértices: {resultado}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
