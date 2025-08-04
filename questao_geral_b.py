# Equipe 05: Letícia Maria Eufrásio Reis, Luis Edurado Sá dos Santos, Maria Luiza Pereira Sousa e Wellison de Oliveira Sousa
# Questão Geral B

import random
import time
import matplotlib.pyplot as plt
import numpy as np

# ALGORITMO DE ORDENAÇÃO
def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

# ALGORITMOS DE BUSCA
def busca_linear_convencional(vetor, chave):
    comparacoes = 0
    for i in range(len(vetor)):
        comparacoes += 1
        if vetor[i] == chave:
            return i, comparacoes
    return -1, comparacoes

def busca_linear_sentinela(vetor, chave):
    tamanho = len(vetor)
    if tamanho == 0:
        return -1, 0
    ultimo_elemento = vetor[tamanho - 1]
    vetor[tamanho - 1] = chave
    i = 0
    comparacoes = 0
    while vetor[i] != chave:
        comparacoes += 1
        i += 1
    vetor[tamanho - 1] = ultimo_elemento
    comparacoes += 1
    if i < tamanho - 1 or vetor[tamanho - 1] == chave:
        return i, comparacoes
    else:
        return -1, comparacoes

def busca_binaria_convencional(vetor, chave):
    comparacoes = [0]
    def _busca(vetor, chave, inicio, fim, comp_ref):
        if inicio <= fim:
            meio = (inicio + fim) // 2
            comp_ref[0] += 1
            if vetor[meio] == chave:
                return meio
            comp_ref[0] += 1
            if chave < vetor[meio]:
                return _busca(vetor, chave, inicio, meio - 1, comp_ref)
            else:
                return _busca(vetor, chave, meio + 1, fim, comp_ref)
        return -1
    indice = _busca(vetor, chave, 0, len(vetor) - 1, comparacoes)
    return indice, comparacoes[0]

def busca_binaria_rapida(vetor, chave):
    inicio, fim = 0, len(vetor) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if vetor[meio] == chave:
            return meio, comparacoes
        comparacoes += 1
        if chave < vetor[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1, comparacoes

# FUNÇÃO PRINCIPAL
def executar_experimento():
    tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
    numero_de_testes_por_tamanho = 50

    # Estruturas para armazenar os resultados finais (médias)
    tempos = {
        'Busca Linear': [], 'Busca Linear Sentinela': [],
        'Busca Binária': [], 'Busca Binária Rápida': []
    }
    comparacoes_resultados = {'Busca Linear': [], 'Busca Binária': []}

    for tamanho in tamanhos:
        print(f"Processando vetor de tamanho {tamanho}...")

        # Otimização: gerar e ordenar os vetores uma única vez por tamanho.
        # A ordenação (operação mais lenta) fica fora do loop de repetição.
        vetor_aleatorio = random.sample(range(0, tamanho * 2), tamanho)
        vetor_ordenado = vetor_aleatorio.copy()
        insertion_sort(vetor_ordenado)

        # Estruturas para armazenar os resultados de cada teste individual
        tempos_testes = {k: [] for k in tempos}
        comparacoes_testes = {k: [] for k in comparacoes_resultados}

        # Loop de repetição para garantir uma média estável
        for _ in range(numero_de_testes_por_tamanho):
            elemento_buscado = random.choice(vetor_aleatorio)

            # --- Testes de Busca Linear ---
            copia_vetor = vetor_aleatorio.copy()
            inicio = time.perf_counter()
            _, comps_bl = busca_linear_convencional(copia_vetor, elemento_buscado)
            fim = time.perf_counter()
            tempos_testes['Busca Linear'].append(fim - inicio)
            comparacoes_testes['Busca Linear'].append(comps_bl)

            copia_vetor = vetor_aleatorio.copy()
            inicio = time.perf_counter()
            busca_linear_sentinela(copia_vetor, elemento_buscado)
            fim = time.perf_counter()
            tempos_testes['Busca Linear Sentinela'].append(fim - inicio)

            # --- Testes de Busca Binária (usam o vetor já ordenado) ---
            inicio = time.perf_counter()
            _, comps_bb = busca_binaria_convencional(vetor_ordenado, elemento_buscado)
            fim = time.perf_counter()
            tempos_testes['Busca Binária'].append(fim - inicio)
            comparacoes_testes['Busca Binária'].append(comps_bb)

            inicio = time.perf_counter()
            busca_binaria_rapida(vetor_ordenado, elemento_buscado)
            fim = time.perf_counter()
            tempos_testes['Busca Binária Rápida'].append(fim - inicio)

        # Cálculo da média dos resultados obtidos nos testes
        for metodo in tempos:
            tempos[metodo].append(np.mean(tempos_testes[metodo]))
        for metodo in comparacoes_resultados:
            comparacoes_resultados[metodo].append(np.mean(comparacoes_testes[metodo]))

    # --- Geração dos Gráficos ---

    # Gráfico 1: Número Médio de Comparações
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, comparacoes_resultados['Busca Linear'], marker='o', label='Busca Linear')
    plt.plot(tamanhos, comparacoes_resultados['Busca Binária'], marker='o', label='Busca Binária')
    plt.title('Número Médio de Comparações vs. Tamanho do Vetor')
    plt.xlabel('Número de elementos (N)')
    plt.ylabel('Número médio de comparações')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico 2: Tempo Médio de Execução
    plt.figure(figsize=(10, 6))
    for metodo, valores in tempos.items():
        plt.plot(tamanhos, valores, marker='o', label=metodo)

    plt.title('Comparativo do Tempo Médio de Execução das Buscas')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Tempo médio de execução (s) - Escala Logarítmica')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.show()


# EXECUÇÃO
executar_experimento()