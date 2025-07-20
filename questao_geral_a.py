# Equipe 05: Letícia Maria Eufrásio Reis, Luis Edurado Sá dos Santos, Maria Luiza Pereira Sousa e Wellison de Oliveira Sousa
# Questão Geral A

import matplotlib.pyplot as plt
import random
import timeit


# Bubble Sort
def bubbleSort(lista):
    i = 0
    n = len(lista)

    while i < n - 1:
        j = 0

        while j < n - 1 - i:
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
            j += 1

        i += 1


# Insertion Sort
def insertionSort(lista):
    i = 1
    n = len(lista)

    while i < n:
        aux = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > aux:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = aux
        i += 1


# Selection Sort
def selectionSort(lista):
    i = 0
    n = len(lista)

    while i < n - 1:
        min = i
        j = i + 1

        while j < n:
            if lista[j] < lista[min]:
                min = j
            j += 1

        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
        i += 1


# Merge Sort
def mergeSort(lista):
    def sort(lista, inicio, fim):
        if inicio < fim:
            meio = (inicio + fim) // 2
            sort(lista, inicio, meio)
            sort(lista, meio + 1, fim)
            merge(lista, inicio, meio, fim)

    def merge(lista, inicio, meio, fim):
        n_esq = meio - inicio + 1
        n_dir = fim - meio

        esq = [0] * n_esq
        dir = [0] * n_dir

        i = 0
        while i < n_esq:
            esq[i] = lista[inicio + i]
            i += 1

        j = 0
        while j < n_dir:
            dir[j] = lista[meio + 1 + j]
            j += 1

        i = 0
        j = 0
        k = inicio

        while i < n_esq and j < n_dir:
            if esq[i] <= dir[j]:
                lista[k] = esq[i]
                i += 1
            else:
                lista[k] = dir[j]
                j += 1
            k += 1

        while i < n_esq:
            lista[k] = esq[i]
            i += 1
            k += 1

        while j < n_dir:
            lista[k] = dir[j]
            j += 1
            k += 1

    n = len(lista)
    sort(lista, 0, n - 1)


# Quick Sort
def quickSort(lista):
    def sort(lista, inicio, fim):
        if inicio < fim:
            p = partition(lista, inicio, fim)
            sort(lista, inicio, p - 1)
            sort(lista, p + 1, fim)

    def partition(lista, inicio, fim):
        pivo = lista[fim]
        i = inicio - 1
        j = inicio

        while j < fim:
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
            j += 1

        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        return i + 1

    n = len(lista)
    sort(lista, 0, n - 1)


# Counting Sort
def countingSort(lista):
    maior = max(lista)
    n = len(lista)

    count = [0] * (maior + 1)
    saida = [0] * n

    i = 0
    while i < n:
        count[lista[i]] += 1
        i += 1

    i = 1
    while i < len(count):
        count[i] += count[i - 1]
        i += 1

    i = n - 1
    while i >= 0:
        num = lista[i]
        count[num] -= 1
        saida[count[num]] = num
        i -= 1

    i = 0
    while i < n:
        lista[i] = saida[i]
        i += 1


# Radix Sort
def radixSort(lista):
    def countingSortDigito(lista, exp):
        n = len(lista)
        count = [0] * 10
        saida = [0] * len(lista)

        i = 0
        while i < n:
            index = (lista[i] // exp) % 10
            count[index] += 1
            i += 1

        i = 1
        while i < 10:
            count[i] += count[i - 1]
            i += 1

        i = n - 1
        while i >= 0:
            index = (lista[i] // exp) % 10
            saida[count[index] - 1] = lista[i]
            count[index] -= 1
            i -= 1

        i = 0
        while i < n:
            lista[i] = saida[i]
            i += 1

    maximo = max(lista)
    exp = 1
    while maximo // exp > 0:
        countingSortDigito(lista, exp)
        exp *= 10


# Bucket Sort
def bucketSort(lista):
    n = len(lista)
    menor = min(lista)
    maior = max(lista)

    buckets = []
    i = 0
    while i < n:
        buckets.append([])
        i += 1

    i = 0
    while i < n:
        norm = (lista[i] - menor) / (maior - menor)
        index = min(int(norm * n), n - 1)
        buckets[index].append(lista[i])
        i += 1

    i = 0
    while i < n:
        insertionSort(buckets[i])
        i += 1

    i = 0
    b = 0
    while b < n:
        j = 0
        while j < len(buckets[b]):
            lista[i] = buckets[b][j]
            i += 1
            j += 1
        b += 1


# Shell Sort
def shellSort(lista):
    n = len(lista)
    intervalo = n // 2

    while intervalo > 0:
        i = intervalo

        while i < n:
            aux = lista[i]
            j = i

            while j >= intervalo and aux < lista[j - intervalo]:
                lista[j] = lista[j - intervalo]
                j -= intervalo

            lista[j] = aux
            i += 1

        intervalo = intervalo // 2



# Heap Sort
def heapSort(lista):
    n = len(lista)

    def heapify(lista, n, i):
        while 2 * i + 1 < n:
            maior = i
            esq = 2 * i + 1
            dir = 2 * i + 2

            if esq < n and lista[esq] > lista[maior]:
                maior = esq

            if dir < n and lista[dir] > lista[maior]:
                maior = dir

            if maior == i:
                break

            lista[i], lista[maior] = lista[maior], lista[i]
            i = maior

    i = n // 2 - 1
    while i >= 0:
        heapify(lista, n, i)
        i -= 1

    i = n - 1
    while i > 0:
        lista[i], lista[0] = lista[0], lista[i]

        heapify(lista, i, 0)
        i -= 1


# Gera uma lista de inteiros de modo aleatório
def geraLista(tam):
    random.seed()
    i = 0
    lista = []

    while i < tam:
        lista.append(random.randint(1, tam))
        i += 1

    return lista


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

temposBubbleSort = []
temposInsertionSort = []
temposSelectionSort = []
temposMergeSort = []
temposQuickSort = []
temposCountingSort = []
temposRadixSort = []
temposBucketSort = []
temposShellSort = []
temposHeapSort = []


for tamanho in tamanhos:
    lista = geraLista(tamanho)

    lista_bubble = list(lista)
    lista_insertion = list(lista)
    lista_selection = list(lista)
    lista_merge = list(lista)
    lista_quick = list(lista)
    lista_counting = list(lista)
    lista_radix = list(lista)
    lista_bucket = list(lista)
    lista_shell = list(lista)
    lista_heap = list(lista)

    tempo = timeit.timeit("bubbleSort({})".format(lista_bubble), setup="from __main__ import bubbleSort", number=1)
    temposBubbleSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Bubble Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("insertionSort({})".format(lista_insertion), setup="from __main__ import insertionSort", number=1)
    temposInsertionSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Insertion Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("selectionSort({})".format(lista_selection), setup="from __main__ import selectionSort", number=1)
    temposSelectionSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Selection Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("mergeSort({})".format(lista_merge), setup="from __main__ import mergeSort", number=1)
    temposMergeSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Merge Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("quickSort({})".format(lista_quick), setup="from __main__ import quickSort", number=1)
    temposQuickSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Quick Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("countingSort({})".format(lista_counting), setup="from __main__ import countingSort", number=1)
    temposCountingSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Counting Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("radixSort({})".format(lista_radix), setup="from __main__ import radixSort", number=1)
    temposRadixSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Radix Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("bucketSort({})".format(lista_bucket), setup="from __main__ import bucketSort", number=1)
    temposBucketSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Bucket Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("shellSort({})".format(lista_shell), setup="from __main__ import shellSort", number=1)
    temposShellSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Shell Sort em {:.3f} segundos".format(tempo))

    tempo = timeit.timeit("heapSort({})".format(lista_heap), setup="from __main__ import heapSort", number=1)
    temposHeapSort.append(tempo)
    print("Lista de tamanho {}".format(tamanho), "ordenada pelo Heap Sort em {:.3f} segundos".format(tempo))

    print("\n")


# Figura 1
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, temposBubbleSort, label="Bubble Sort", color="blue", marker='o')
plt.plot(tamanhos, temposInsertionSort, label="Insertion Sort", color="red", marker='o')
plt.plot(tamanhos, temposSelectionSort, label="Selection Sort", color="green", marker='o')
plt.plot(tamanhos, temposMergeSort, label="Merge Sort", color="grey", marker='o')
plt.plot(tamanhos, temposQuickSort, label="Quick Sort", color="magenta", marker='o')
plt.plot(tamanhos, temposCountingSort, label="Counting Sort", color="orange", marker='o')
plt.plot(tamanhos, temposRadixSort, label="Radix Sort", color="gold", marker='o')
plt.plot(tamanhos, temposBucketSort, label="Bucket Sort", color="deepskyblue", marker='o')
plt.plot(tamanhos, temposShellSort, label="Shell Sort", color="darkblue", marker='o')
plt.plot(tamanhos, temposHeapSort, label="Heap Sort", color="lime", marker='o')

plt.title("Análise de Tempo - Algoritmos de Ordenação")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n")

# Figura 2
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, temposMergeSort, label="Merge Sort", color="grey", marker='o')
plt.plot(tamanhos, temposQuickSort, label="Quick Sort", color="magenta", marker='o')
plt.plot(tamanhos, temposCountingSort, label="Counting Sort", color="orange", marker='o')
plt.plot(tamanhos, temposRadixSort, label="Radix Sort", color="gold", marker='o')
plt.plot(tamanhos, temposBucketSort, label="Bucket Sort", color="deepskyblue", marker='o')
plt.plot(tamanhos, temposShellSort, label="Shell Sort", color="darkblue", marker='o')
plt.plot(tamanhos, temposHeapSort, label="Heap Sort", color="lime", marker='o')

plt.title("Algoritmos com tempo de execução < 1 segundo")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()