
def diferenca_entre_caminhoes(caminhoes):
    return max(caminhoes) - min(caminhoes)

def distribuir_rotas_divisao_conquista(rotas, num_caminhoes):
    if len(rotas) == 0:
        return [[] for _ in range(num_caminhoes)]

    rotas.sort(reverse=True)

    return divide_rotas(rotas, num_caminhoes)


def divide_rotas(rotas, num_caminhoes):
    if len(rotas) == 0:
        return [[] for _ in range(num_caminhoes)]

    if num_caminhoes == 1:
        return [rotas]

    melhor_distribuicao = None
    menor_diferenca = float('inf')

    for i in range(1, len(rotas)):
        distribuicao_atual = [rotas[:i]] + divide_rotas(rotas[i:], num_caminhoes - 1) or [[] for _ in range(num_caminhoes - 1)]

        quilometragens = [sum(rota) for rota in distribuicao_atual]
        diferenca = diferenca_entre_caminhoes(quilometragens)

        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            melhor_distribuicao = distribuicao_atual

    return melhor_distribuicao or [[] for _ in range(num_caminhoes)]
