def isBetween(kmMedia, tamDiferenca, valor):
    limiteInferior = round(kmMedia * (1 - tamDiferenca), 2)
    limiteSuperior = round(kmMedia * (1 + tamDiferenca), 2)
    retorno = False

    if limiteInferior <= valor <= limiteSuperior:
        retorno = True
    
    return retorno

def diferenca_entre_caminhoes(caminhoes):
    return max(caminhoes) - min(caminhoes)

def distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, melhor_distribuicao, iterator):
    if (num_caminhoes - iterator) == 1:
        melhor_distribuicao[iterator] = rotas
        return
    m = len(rotas) + 1
    n = num_caminhoes + 1
    linha = coluna = 0

    # Inicializa a matriz de programação dinâmica
    prog_din = [[0] * (n) for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            prog_din[i][j] = max(prog_din[i-1][j], prog_din[i-1][j-1] + rotas[i-1])
            if isBetween(kmMedia, tamDiferenca, prog_din[i][j]):
                linha = i-1
                coluna = j-1
                i = m
                j = n
                break
        if (linha != 0 and coluna != 0):
            break

    melhor_distribuicao[iterator].append(rotas[linha])
    rotas[linha] = -1

    while linha > 0 and coluna > 0: 
        if prog_din[linha][coluna] == prog_din[linha-1][coluna]:
            melhor_distribuicao[iterator].append(rotas[linha-1])
            rotas[linha-1] = -1
            linha = linha - 1
        else:
            if rotas[linha-1] > 0:
                melhor_distribuicao[iterator].append(rotas[linha-1])
                rotas[linha-1] = -1
            linha = linha - 1
            coluna = coluna - 1

    for x in rotas.copy():
        if x == -1:
            rotas.remove(x)

    distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, melhor_distribuicao, iterator = iterator + 1)

def distribuir_rotas_backtracking(rotas, num_caminhoes):
    kmMedia = sum(rotas)/num_caminhoes
    tamDiferenca = 0.10
    melhor_distribuicao = [[] * len(rotas) for _ in range(num_caminhoes)]
    distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, melhor_distribuicao, 0)
    
    return melhor_distribuicao

num_caminhoes = 3
rotas = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]
result = distribuir_rotas_backtracking(rotas, num_caminhoes)

# Execução local
'''
kmMedia = sum(rotas)/num_caminhoes
tamDiferenca = 0.10

melhor_distribuicao = [[] * len(rotas) for _ in range(num_caminhoes)]
distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, melhor_distribuicao, 0)
print(melhor_distribuicao)'''