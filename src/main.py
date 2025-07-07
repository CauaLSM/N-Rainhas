from tabuleiro import criar_estado_inicial, contar_conflitos, printar_tabuleiro
from busca_HC import hill_climbing_com_reinicio


def main():
    n = int(input("Digite o tamanho do tabuleiro (n): "))
    linha = input("Digite o estado inicial (colunas separadas por espaço),\n" "ou apenas pressione Enter para gerar aleatório: ")
    
    if linha.strip():
        estado = list(map(int, linha.split()))
        if len(estado) != n:
            print(f"Erro: você digitou {len(estado)} valores, mas N = {n}.")
            return
    else:
        estado = criar_estado_inicial(n)

    print("\n=== Estado Inicial ===")
    printar_tabuleiro(estado)
    print("Conflitos iniciais:", contar_conflitos(estado), "\n")

    solucao_busca = hill_climbing_com_reinicio(n)
    print("=== Após Busca (Hill Climbing) ===")
    printar_tabuleiro(solucao_busca)
    conflitos_busca = contar_conflitos(solucao_busca)
    print("Conflitos após busca:", conflitos_busca, "\n")

if __name__ == "__main__":
    main()