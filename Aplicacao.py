from matplotlib import pyplot as plt
import networkx as nx
from guloso.Guloso import distribuir_rotas_guloso, distribuir_rotas_guloso_ord
from GeradorDeProblemas import GeradorDeProblemas


def main():
    num_caminhoes = 3
    conjunto = GeradorDeProblemas.geracaoDeRotas(21, 3, 4)
    for rotas in conjunto:
        print(rotas)
        algoritmoGuloso(rotas, num_caminhoes)
         


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


if __name__ == "__main__":
    main()