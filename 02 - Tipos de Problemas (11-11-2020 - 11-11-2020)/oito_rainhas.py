'''
Desenvoldido por: Clésio de Araújo Gonçalves
'''

import numpy as np
from itertools import permutations

# Variáveis de controle
n = 8 # Numero de rainhas
indice_linha, indice_coluna = 0, 0
diagonais_atendem_restricoes, qnt_permutacoes_geradas, qnt_tabuleiros_validos = 0, 0, 0
tabuleiros = []

# Gera as permutações com todas as possibilidades da matriz
array = range(n)
linhas_xadrez = permutations(array)

# Gera a matriz xadrez
matriz_xadrez = np.zeros((n,n), dtype=np.int32)

# Cria todos os tabuleiros de xadrez com as rainhas dispostas
# A permutação atende as restrições em linhas e colunas (exceto diagonais)
for linha_xadrez in linhas_xadrez:
    for posicao_linha in linha_xadrez:
        matriz_xadrez[posicao_linha, indice_coluna] = 1
        indice_coluna += 1
    indice_coluna = 0
    tabuleiros.append(matriz_xadrez)
    matriz_xadrez = np.zeros((n, n), dtype=int)
    qnt_permutacoes_geradas +=1
print("Quantidade de permutações geradas: ", qnt_permutacoes_geradas)

# Valida os tabuleiros de xadrez com a ordem correta das rainhas dispostas
for tabuleiro in tabuleiros:
    for linha in tabuleiro:
        for elemento in linha:
            if (elemento == 1): # Só verifica as posições do tabuleiro que possuem rainha
                diagonal_principal = np.diagonal(tabuleiro, indice_coluna - indice_linha)
                diagonal_secundaria = np.fliplr(tabuleiro).diagonal(((n - 1) - indice_coluna) - indice_linha)

                if sum(diagonal_principal) == 1: # Se a diagonal principal não for igual a 1, então ele nem testa a diagonal secundária
                    if sum(diagonal_secundaria) == 1:
                        diagonais_atendem_restricoes += 1

            # Continua varrendo cada elemento da mesma linha
            indice_coluna += 1

        # Apos todos os elementos da linha, passa para a proxima linha
        indice_linha += 1
        indice_coluna = 0

    # Apos todas as linhas do tabuleiro, reinicia variavel para o proximo tabuleiro
    indice_linha = 0

    if diagonais_atendem_restricoes == n:
        qnt_tabuleiros_validos += 1
        print(tabuleiro)
        print("-----------------------")

    diagonais_atendem_restricoes = 0

print("Quantidade de tabuleiros válidos: ", qnt_tabuleiros_validos)
