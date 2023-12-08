import sys

def diferenca_entre_caminhoes(caminhoes):
    return max(caminhoes) - min(caminhoes)

def distribuir_rotas_backtracking(rotas, num_caminhoes):
    melhor_diferenca = sys.maxsize
    melhor_distribuicao = []

    def distribuicao_recursiva(distribuicao_atual, index_rota):
        nonlocal melhor_diferenca, melhor_distribuicao

        if index_rota == len(rotas):
            diferenca_atual = diferenca_entre_caminhoes([sum(caminhao) for caminhao in distribuicao_atual])
            if diferenca_atual < melhor_diferenca:
                melhor_diferenca = diferenca_atual
                melhor_distribuicao = [caminhao[:] for caminhao in distribuicao_atual]
            return

        for i in range(num_caminhoes):
            distribuicao_atual[i].append(rotas[index_rota])

            if not poda(distribuicao_atual, index_rota + 1, melhor_diferenca, rotas):
                distribuicao_recursiva(distribuicao_atual, index_rota + 1)

            distribuicao_atual[i].pop()

    distribuicao_recursiva([[] for _ in range(num_caminhoes)], 0)
    return melhor_distribuicao, melhor_diferenca

def poda(distribuicao_atual, index_rota, melhor_diferenca, sizeRotas):
    quilometragem_caminhoes = [sum(caminhao) for caminhao in distribuicao_atual]

    # Verifica se a distribuição parcial já é pior que a melhor solução encontrada
    if diferenca_entre_caminhoes(quilometragem_caminhoes) >= melhor_diferenca:
        return True

    if index_rota < len(sizeRotas):
        # Verifica se a diferença parcial já é menor ou igual à melhor diferença encontrada
        quilometragem_caminhoes.sort()
        return diferenca_entre_caminhoes(quilometragem_caminhoes) >= melhor_diferenca
    else:
        return diferenca_entre_caminhoes(quilometragem_caminhoes) >= melhor_diferenca
