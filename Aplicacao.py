import time
from matplotlib import pyplot as plt
import networkx as nx
from guloso.Guloso import distribuir_rotas_guloso, distribuir_rotas_guloso_ord
from backtracking.Backtracking import distribuir_rotas_backtracking
from GeradorDeProblemas import GeradorDeProblemas


def main():
    contador = 1
    qtd_rotas = 6
    num_caminhoes = 3
    
    while True:
        conjunto = GeradorDeProblemas.geracaoDeRotas(qtd_rotas, contador, 4)
        tempo_medio = medir_tempo_execucao(conjunto, num_caminhoes, contador)
        print(f"Tamanho do conjunto: {contador}, Tempo médio: {tempo_medio:.6f} segundos")
        # algoritmoGuloso(rotas, num_caminhoes)
        backtracking(conjunto, num_caminhoes)
        
        if tempo_medio > 30:
            break

        qtd_rotas += 1
        # contador+=1
        # if contador % 10 == 0:
        #     qtd_rotas+=1
         


def algoritmoGuloso(rotas, num_caminhoes):
    print(f'----------------------- GULOSO -----------------------\n')
    
    distribuicao, diferenca = distribuir_rotas_guloso_ord(rotas, num_caminhoes)
    
    for i, caminhao in enumerate(distribuicao):
        print(f'Caminhão {i + 1}: {caminhao}')
    print(f'Menor diferença de quilometragem: {diferenca} km')
    
    distribuicao, diferenca = distribuir_rotas_guloso(rotas, num_caminhoes)

    # Imprima a distribuição e a diferença de quilometragem
    for i, caminhao in enumerate(distribuicao):
        print(f'Caminhão {i + 1}: {caminhao}')
    print(f'Menor diferença de quilometragem: {diferenca} km')
    
    
def backtracking(rotas, num_caminhoes):
    print(f'----------------------- BACKTRACKING -----------------------\n')
    
    for rota in rotas:
        melhor_distribuicao, melhor_diferenca = distribuir_rotas_backtracking(rota, num_caminhoes)

        print("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:")
        for i, caminhao in enumerate(melhor_distribuicao):
            print(f"Caminhão {i + 1}: {caminhao}")
        print(f"Diferença mínima de quilometragem: {melhor_diferenca} km")
    
def medir_tempo_execucao(rotas, num_caminhoes, tamanho_conjunto):
    tempos_execucao = []

    for _ in range(10):  # Testar 10 vezes para calcular a média
        inicio = time.time()
        backtracking(rotas[:tamanho_conjunto], num_caminhoes)
        fim = time.time()
        tempos_execucao.append(fim - inicio)

    tempo_medio = sum(tempos_execucao) / len(tempos_execucao)
    return tempo_medio


if __name__ == "__main__":
    main()