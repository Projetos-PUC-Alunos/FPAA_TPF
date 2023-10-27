import itertools

def distruir_rotas_forca_bruta(rotas, num_caminhoes):
    todas_combinacoes = list(itertools.combinations(rotas, len(rotas)))
    menor_diferenca = float('inf')

    for combinacao in todas_combinacoes:
        permutacoes = itertools.permutations(combinacao)
        
        for permutacao in permutacoes:
            distribuicoes = [list(permutacao[i::num_caminhoes]) for i in range(num_caminhoes)]
            
            quilometragens = [sum(distribuicao) for distribuicao in distribuicoes]
            diferenca = max(quilometragens) - min(quilometragens)
            
            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                melhor_distribuicao = distribuicoes

    return melhor_distribuicao, menor_diferenca

