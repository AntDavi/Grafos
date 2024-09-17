import numpy as np
import time
from scipy.optimize import linear_sum_assignment

# Função para resolver o problema de emparelhamento máximo com o algoritmo Húngaro
def algoritmo_hungaro(matriz_custo):
    # Resolvendo o problema com o algoritmo Húngaro
    row_ind, col_ind = linear_sum_assignment(matriz_custo)
    custo_total = matriz_custo[row_ind, col_ind].sum()
    
    # Retornando os índices das linhas e colunas para o emparelhamento ótimo e o custo total
    return row_ind, col_ind, custo_total

# Exemplo de matriz de custo
matriz_custo = np.array([
    [4, 1, 3],
    [2, 0, 5],
    [3, 2, 2]
])

# Medindo o tempo de execução
inicio = time.time()  # Marca o início
linhas, colunas, custo_total = algoritmo_hungaro(matriz_custo)
fim = time.time()  # Marca o fim

# Exibindo o emparelhamento ótimo e o custo total
print(f"Emparelhamento ótimo (linhas para colunas): {list(zip(linhas, colunas))}")
print(f"Custo total: {custo_total}")
print(f"Tempo de execução: {fim - inicio:.6f} segundos")