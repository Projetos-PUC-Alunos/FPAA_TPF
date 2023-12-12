def isBetween(kmMedia, tamDiferenca, valor):
    limiteInferior = round(kmMedia * (1 - tamDiferenca))
    limiteSuperior = round(kmMedia * (1 + tamDiferenca))
    retorno = False

    if limiteInferior <= valor <= limiteSuperior:
        retorno = True

    return retorno

def distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, distribuicao, iterator, tamColuna):
    if iterator == num_caminhoes-1:
        distribuicao[iterator] = rotas
        return
    
    m = len(rotas)

    progDin = [[0] * (tamColuna + 1) for _ in range(m + 1)]
    # Inicializar a primeira coluna com '.'
    for i in range(1, m+1):
        progDin[i][0] = '.'
    # Inicializar a primeira linha com 'F'
    for j in range(1, tamColuna+1):
        progDin[0][j] = 'F'
        
    # Inicializar primeiro elemento da matriz com 'V'
    progDin[0][0] = 'V'
    
    i = j = 1
    linha = coluna = 0

    while i < m+1:
        j = 1
        while j < tamColuna+1:
            if progDin[i-1][j] == 'V':
                progDin[i][j] = '.'
            elif progDin[i-1][j-rotas[i-1]] == 'V':
                progDin[i][j] = 'V'
                if isBetween(kmMedia, tamDiferenca, j):
                    linha, coluna = i, j
                    i, j = m, tamColuna
            else:
                progDin[i][j] = 'F'
            
            j += 1
        i += 1


    while linha > 0 and coluna > 0:
        if progDin[linha][coluna] == 'V':
            distribuicao[iterator].append(rotas[linha-1])
            coluna -= rotas[linha-1]
            rotas[linha-1] = -1
            linha -= 1
        elif progDin[linha][coluna] == '.':
            linha -= 1

    for x in rotas.copy():
        if x == -1:
            rotas.remove(x)

    iterator+=1
    distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, distribuicao, iterator, tamColuna)


def distribuir_rotas_dinamica(rotas, num_caminhoes):
    rotasCopia = rotas.copy()
    rotasCopia.sort()
    kmMedia = sum(rotasCopia)/num_caminhoes
    tamDiferenca = 0.10
    tamColuna = round(kmMedia * (1 + tamDiferenca))
    distribuicao = [[] for _ in range(num_caminhoes)]
    distribuir_rotas(rotasCopia, num_caminhoes, kmMedia, tamDiferenca, distribuicao, 0, tamColuna)

    return distribuicao

# Execução Local
'''
num_caminhoes = 3
#rotas = [35, 34, 33, 23, 21, 32, 35, 19, 26, 42]
#rotas = [40, 36, 38, 29, 32, 28, 31, 35, 31, 30, 32, 30, 29, 39, 35, 38, 39, 35, 32, 38, 32, 33, 29, 33, 29, 39, 28]
rotas = [32, 51, 32, 43, 42, 30, 42, 51, 43, 51, 29, 25, 27, 32, 29, 55, 43, 29, 32, 44, 55, 29, 53, 30, 24, 27]
melhor_distribuicao = distribuir_rotas_dinamica(rotas, num_caminhoes)
'''