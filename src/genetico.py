import random
from tabuleiro import contar_conflitos

def criar_populacao(tamanho_pop, n):
    return [ [random.randint(0, n - 1) for _ in range(n)] for _ in range(tamanho_pop) ]

def fitness(estado):
    n = len(estado)
    max_conflitos = (n * (n - 1)) // 2
    return max_conflitos - contar_conflitos(estado)

def selecionar(populacao):
    pesos = [fitness(ind) for ind in populacao]
    return random.choices(populacao, weights=pesos, k=2)

def cruzar(p1, p2):
    n = len(p1)
    ponto = random.randint(1, n - 2)
    filho = p1[:ponto] + p2[ponto:]
    return filho

def mutar(individuo, taxa_mutacao):
    n = len(individuo)
    if random.random() < taxa_mutacao:
        i = random.randint(0, n - 1)
        individuo[i] = random.randint(0, n - 1)
    return individuo

def algoritmo_genetico(n, tamanho_pop=100, taxa_mutacao=0.03, max_geracoes=1000):
    maxFitness = (n * (n - 1)) // 2
    populacao = criar_populacao(tamanho_pop, n)
    for geracao in range(max_geracoes):
        populacao = sorted(populacao, key=lambda x: fitness(x), reverse=True)
        if fitness(populacao[0]) == maxFitness:
            print(f"Solução encontrada na geração {geracao}!")
            return populacao[0]
        
        nova_populacao = []
        while len(nova_populacao) < tamanho_pop:
            p1, p2 = selecionar(populacao)
            filho = cruzar(p1, p2)
            filho = mutar(filho, taxa_mutacao)
            nova_populacao.append(filho)
        populacao = nova_populacao
    print("Solução aproximada após número máximo de gerações.")
    return populacao[0]
