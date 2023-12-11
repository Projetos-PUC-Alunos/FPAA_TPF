def distribuir_rotas_dinamica(rotas, num_caminhoes):
    qtd_rotas = len(rotas)

    prog_din = [[float('inf')] * (qtd_rotas + 1) for _ in range(num_caminhoes + 1)]
    prog_din[0][0] = 0

    for i in range(1, num_caminhoes + 1):
        for j in range(1, qtd_rotas + 1):
            prog_din[i][j] = min(prog_din[i][j-1], prog_din[i-1][j-1] + rotas[j-1])
    

    melhor_distribuicao = [[] for _ in range(num_caminhoes)]
    copia_num_caminhoes = num_caminhoes 
    copia_qtd_rotas = qtd_rotas


    while copia_qtd_rotas > 0:
        melhor_distribuicao[copia_num_caminhoes-1].append(rotas[copia_qtd_rotas-1])

        if copia_num_caminhoes <= 1:
            copia_num_caminhoes = num_caminhoes
        else:
            copia_num_caminhoes = copia_num_caminhoes - 1
        copia_qtd_rotas -= 1

    return melhor_distribuicao
