import random
from tabuleiro import contar_conflitos, criar_estado_inicial

def gerar_vizinhos(estado):
    vizinhos = []
    n = len(estado)
    for coluna in range(n):
        for linha in range(n):
            if estado[coluna] != linha:
                novo_estado = estado.copy()
                novo_estado[coluna] = linha
                vizinhos.append(novo_estado)
    return vizinhos

def escolher_melhor_vizinho(vizinhos):
    melhor = vizinhos[0]
    menor_conflito = contar_conflitos(melhor)
    for vizinho in vizinhos[1:]:
        conflitos = contar_conflitos(vizinho)
        if conflitos < menor_conflito:
            melhor = vizinho
            menor_conflito = conflitos
    return melhor

def hill_climbing(n):
    atual = criar_estado_inicial(n)
    while True:
        vizinhos = gerar_vizinhos(atual)
        melhor_vizinho = escolher_melhor_vizinho(vizinhos)
        if contar_conflitos(melhor_vizinho) >= contar_conflitos(atual):
            return atual  
        atual = melhor_vizinho

def hill_climbing_com_reinicio(n, max_reinicios=500):
    for _ in range(max_reinicios):
        solucao = hill_climbing(n)
        if contar_conflitos(solucao) == 0:
            return solucao
    return solucao  


