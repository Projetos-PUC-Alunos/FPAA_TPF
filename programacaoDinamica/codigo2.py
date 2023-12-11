'''
Este código apresentou falhas ao exibir o resultado em alguns conjuntos de teste, dos conjuntos que se 
iniciam pelo último conjunto do Backtracking. 
'''

def isBetween(kmMedia, tamDiferenca, valor):
    limiteInferior = round(kmMedia * (1 - tamDiferenca), 2)
    limiteSuperior = round(kmMedia * (1 + tamDiferenca), 2)
    retorno = False

    if limiteInferior <= valor <= limiteSuperior:
        retorno = True

    return retorno

def distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, distribuicao, iterator):
    if iterator == num_caminhoes-1:
        distribuicao[iterator] = rotas
        return
    m = len(rotas)
    linha = coluna = 0

    dp = [[0] * (m + 1) for _ in range(num_caminhoes + 1)]

    for i in range(1, num_caminhoes + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1] + rotas[j-1])
            if isBetween(kmMedia, tamDiferenca, dp[i][j]):
                linha, coluna = i, j
                break
            if j == m and i == num_caminhoes:
                linha, coluna = i, j
        if linha > 0 and coluna > 0:
            break
    
    while coluna > 0:
        if (dp[linha][coluna] - dp[linha][coluna-1]) == rotas[coluna-1]:
            distribuicao[iterator].append(rotas[coluna-1])
            rotas[coluna-1] = -1
        coluna -= 1

    for x in rotas.copy():
        if x == -1:
            rotas.remove(x)

    iterator+=1
    distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, distribuicao, iterator)
    

def distribuir_rotas_dinamica(rotas, num_caminhoes):
    kmMedia = sum(rotas)/num_caminhoes
    tamDiferenca = 0.15
    distribuicao = [[] for _ in range(num_caminhoes)]
    distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, distribuicao, 0)

# Execução Local
num_caminhoes = 3
rotas = [40, 36, 38, 29, 32, 28, 31, 35, 31, 30, 32, 30, 29, 39, 35, 38, 39, 35, 32, 38, 32, 33, 29, 33, 29, 39, 28]
print(sum(rotas))
kmMedia = sum(rotas)/num_caminhoes
tamDiferenca = 0.15
distribuicao = [[] for _ in range(num_caminhoes)]
distribuir_rotas(rotas, num_caminhoes, kmMedia, tamDiferenca, distribuicao, 0)
for idx, caminhao in enumerate(distribuicao):
    total_kms = sum(caminhao)
    print(f'Caminhão {idx + 1}: rotas {", ".join(map(str, caminhao))} - total {total_kms}km')