from matplotlib import pyplot as plt
import networkx as nx
from forcabruta.Forca_Bruta import distruir_rotas_forca_bruta
from guloso.Guloso import distribuir_rotas_guloso


def main():
    rotas = [14, 17, 11, 19, 23, 16, 18, 13, 22, 26, 15]
    num_caminhoes = 3
    
    algoritmoForcaBruta(rotas, num_caminhoes)

    algoritmoGuloso(rotas, num_caminhoes)


def algoritmoForcaBruta(rotas, num_caminhoes):
    print(f'----------------------- FORCA BRUTA -----------------------\n')
    
    # Inicialize a menor diferença como infinito
    menor_diferenca = float('inf')

    # Inicialize a melhor distribuição como uma lista vazia
    melhor_distribuicao = []

    # Gere todas as combinações possíveis das rotas
    melhor_distribuicao, menor_diferenca = distruir_rotas_forca_bruta(rotas, num_caminhoes)

    for i, caminhao in enumerate(melhor_distribuicao):
        print(f'Caminhão {i + 1}: {caminhao}')
    print(f'Menor diferença de quilometragem: {menor_diferenca} km')
        

    

def algoritmoGuloso(rotas, num_caminhoes):
    print(f'----------------------- GULOSO -----------------------\n')
    
    distribuicao, diferenca = distribuir_rotas_guloso(rotas, num_caminhoes)

    # Imprima a distribuição e a diferença de quilometragem
    for i, caminhao in enumerate(distribuicao):
        print(f'Caminhão {i + 1}: {caminhao}')
    print(f'Menor diferença de quilometragem: {diferenca} km')


if __name__ == "__main__":
    main()