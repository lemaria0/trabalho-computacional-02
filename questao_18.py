# Equipe 05: Letícia Maria Eufrásio Reis, Luis Edurado Sá dos Santos, Maria Luiza Pereira Sousa e Wellison de Oliveira Sousa
# Questão 18

# Define a estrutura de um nó da lista encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# Insere um novo nó no final da lista encadeada
def inserir_final(inicio, valor):
    novo_no = Node(valor)
    if inicio is None:
        return novo_no
    atual = inicio
    while atual.proximo:
        atual = atual.proximo
    atual.proximo = novo_no
    return inicio

# Exibe os elementos da lista encadeada no console
def exibir_lista(inicio):
    atual = inicio
    while atual:
        print(atual.valor, end=' -> ')
        atual = atual.proximo
    print('None')

# Divide a lista encadeada em duas metades
def dividir_meio(cabeca):
    if cabeca is None or cabeca.proximo is None:
        return cabeca, None
    lento = cabeca
    rapido = cabeca.proximo
    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo
    meio = lento.proximo
    lento.proximo = None
    return cabeca, meio

# Mescla duas listas encadeadas ordenadas
def mesclar_esq_dir(esq, dir):
    if not esq:
        return dir
    if not dir:
        return esq
    if esq.valor <= dir.valor:
        resultado = esq
        resultado.proximo = mesclar_esq_dir(esq.proximo, dir)
    else:
        resultado = dir
        resultado.proximo = mesclar_esq_dir(esq, dir.proximo)
    return resultado

# Aplica o Merge Sort na lista encadeada
def merge_sort_lista(cabeca):
    if cabeca is None or cabeca.proximo is None:
        return cabeca
    esquerda, direita = dividir_meio(cabeca)
    esquerda = merge_sort_lista(esquerda)
    direita = merge_sort_lista(direita)
    return mesclar_esq_dir(esquerda, direita)

# Programa principal
if __name__ == "__main__":
    print("Digite os números para a lista (separados por espaço):")
    entrada = input("→ ").strip()

    if entrada == "":
        print("Nenhum número foi digitado.")
    else:
        numeros = list(map(int, entrada.split()))
        inicio = None
        for num in numeros:
            inicio = inserir_final(inicio, num)

        print("\nLista original:")
        exibir_lista(inicio)

        # Ordena a lista
        inicio = merge_sort_lista(inicio)

        print("\nLista ordenada:")
        exibir_lista(inicio)