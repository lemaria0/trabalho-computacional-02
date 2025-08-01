# Equipe 05: Letícia Maria Eufrásio Reis, Luis Edurado Sá dos Santos, Maria Luiza Pereira Sousa e Wellison de Oliveira Sousa
# Questão 19

import time

# Define um nó da lista duplamente encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None

# Define a estrutura da lista duplamente encadeada
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None

    # Inserção ordenada
    def inserir(self, valor):
        novo = Node(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            anterior = None
            while atual and atual.valor < valor:
                anterior = atual
                atual = atual.prox
            if anterior is None:
                novo.prox = self.inicio
                self.inicio.ant = novo
                self.inicio = novo
            else:
                novo.prox = atual
                novo.ant = anterior
                anterior.prox = novo
                if atual:
                    atual.ant = novo

    # Exibe a lista
    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.valor, end=' <-> ')
            atual = atual.prox
        print("None")

    # Busca sequencial simples
    def busca_sequencial(self, valor):
        atual = self.inicio
        while atual:
            if atual.valor == valor:
                return atual
            atual = atual.prox
        return None

    # Busca binária simulada em lista duplamente encadeada
    def busca_binaria(self, valor):
        def get_meio(inicio, fim):
            lento = inicio
            rapido = inicio
            while rapido != fim and rapido and rapido.prox != fim:
                rapido = rapido.prox
                if rapido != fim and rapido:
                    rapido = rapido.prox
                    lento = lento.prox
            return lento

        inicio = self.inicio
        fim = None
        iteracoes = 0
        max_iter = 1000  # segurança contra loop infinito

        while inicio != fim and iteracoes < max_iter:
            meio = get_meio(inicio, fim)
            if not meio:
                return None
            if meio.valor == valor:
                return meio
            elif meio.valor < valor:
                inicio = meio.prox
            else:
                fim = meio
            iteracoes += 1

        return None


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    lista = ListaDuplamenteEncadeada()

    entrada = input("Digite os números da lista (separados por espaço): ")
    valores = sorted(map(int, entrada.strip().split()))  # garantir ordenação

    for v in valores:
        lista.inserir(v)

    print("\nLista ordenada:")
    lista.exibir()

    valor_busca = int(input("\nDigite um valor para buscar: "))

    # BUSCA SEQUENCIAL
    t1 = time.perf_counter()
    resultado_seq = lista.busca_sequencial(valor_busca)
    t2 = time.perf_counter()
    tempo_seq = t2 - t1

    # BUSCA BINÁRIA (simulada)
    t3 = time.perf_counter()
    resultado_bin = lista.busca_binaria(valor_busca)
    t4 = time.perf_counter()
    tempo_bin = t4 - t3

    # RESULTADOS
    print("\n[Busca Sequencial]")
    print("Resultado:", "Encontrado!" if resultado_seq else "Não encontrado.")
    print(f"Tempo: {tempo_seq:.8f} segundos")

    print("\n[Busca Binária]")
    print("Resultado:", "Encontrado!" if resultado_bin else "Não encontrado.")
    print(f"Tempo: {tempo_bin:.8f} segundos")

    # Comparação
    if tempo_seq < tempo_bin:
        print("\n→ A busca sequencial foi mais rápida.")
    elif tempo_seq > tempo_bin:
        print("\n→ A busca binária foi mais rápida.")
    else:
        print("\n→ Ambas as buscas tiveram tempos iguais.")