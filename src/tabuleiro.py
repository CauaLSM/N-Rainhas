import random

def criar_estado_inicial(n):
    estado = list(range(n))
    random.shuffle(estado)
    return estado

def contar_conflitos(estado):
    n = len(estado)
    conflitos = 0
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def printar_tabuleiro(estado):
    n = len(estado)
    for linha in range(n):
        linha_visual = ['.'] * n
        linha_visual[estado[linha]] = 'Q'
        print(' '.join(linha_visual))
    print()
