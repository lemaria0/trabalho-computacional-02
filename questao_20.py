class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

# Construção da árvore:
#         10
#       /  |  \
#     2    3   4
#         / \
#        5   6

raiz = No(10)
filho1 = No(2)
filho2 = No(3)
filho3 = No(4)
filho2.filhos = [No(5), No(6)]
raiz.filhos = [filho1, filho2, filho3]

def contar_nos_rec(no):
    if no is None:
        return 0
    return 1 + sum(contar_nos_rec(filho) for filho in no.filhos)

def contar_nos_iter(raiz):
    if raiz is None:
        return 0
    pilha = [raiz]
    contador = 0
    while pilha:
        atual = pilha.pop()
        contador += 1
        pilha.extend(atual.filhos)
    return contador

def somar_nos_rec(no):
    if no is None:
        return 0
    return no.valor + sum(somar_nos_rec(filho) for filho in no.filhos)

def somar_nos_iter(raiz):
    if raiz is None:
        return 0
    pilha = [raiz]
    soma = 0
    while pilha:
        atual = pilha.pop()
        soma += atual.valor
        pilha.extend(atual.filhos)
    return soma

def profundidade_rec(no):
    if no is None:
        return 0
    if not no.filhos:
        return 1
    return 1 + max(profundidade_rec(filho) for filho in no.filhos)

from collections import deque

def profundidade_iter(raiz):
    if raiz is None:
        return 0
    fila = deque([(raiz, 1)])
    max_profundidade = 0
    while fila:
        atual, prof = fila.popleft()
        max_profundidade = max(max_profundidade, prof)
        for filho in atual.filhos:
            fila.append((filho, prof + 1))
    return max_profundidade


print("Número de nós (rec):", contar_nos_rec(raiz))
print("Número de nós (iter):", contar_nos_iter(raiz))

print("Soma dos nós (rec):", somar_nos_rec(raiz))
print("Soma dos nós (iter):", somar_nos_iter(raiz))

print("Profundidade (rec):", profundidade_rec(raiz))
print("Profundidade (iter):", profundidade_iter(raiz))