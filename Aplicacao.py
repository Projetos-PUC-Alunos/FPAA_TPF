import time
from backtracking.Backtracking import distribuir_rotas_backtracking
from GeradorDeProblemas import GeradorDeProblemas
from divisaoconquista.Divisao_Conquista import distribuir_rotas_divisao_conquista
from divisaoconquista.Divisao_Conquista import diferenca_entre_caminhoes
from programacaoDinamica.programacaoDinamica import distribuir_rotas_dinamica

def main():
    qtd_rotas = 6
    qtd_conjunto = 10
    dispersao = 75
    whileTime = True
    iterator = 0
    
    conjuntoResultante = []
    
    # WhileTime para execução do gerador de problemas para o backtracking
    while whileTime:
        conjunto = GeradorDeProblemas.geracaoDeRotas(qtd_rotas, qtd_conjunto, dispersao)
        whileTime, conjuntoResultante = medir_tempo_execucao(qtd_rotas, conjunto, dispersao, 3)

        qtd_rotas += 1
    
    # Conjuntos de rotas fornecidos
    rotas1 = [40, 36, 38, 29, 32, 28, 31, 35, 31, 30, 32, 30, 29, 39, 35, 38, 39, 35, 32, 38, 32, 33, 29, 33, 29, 39, 28]
    rotas2 = [32, 51, 32, 43, 42, 30, 42, 51, 43, 51, 29, 25, 27, 32, 29, 55, 43, 29, 32, 44, 55, 29, 53, 30, 24, 27]

    # # Adicione os conjuntos de rotas à lista de testes
    rotas_teste = [rotas1, rotas2]

    divisaoconquista(rotas_teste, 3)
    
    qtd_rotas -= 1
    qtd_rotas_T = qtd_rotas
    
    arquivo = open('progDin.txt', 'w')
    while iterator < 10:
        medir_tempo_prog_dinamica(qtd_rotas, conjuntoResultante, 3, arquivo)
        qtd_rotas += qtd_rotas_T
        conjuntoResultante = GeradorDeProblemas.geracaoDeRotas(qtd_rotas, qtd_conjunto, dispersao)
        iterator += 1
    programacaodinamica(rotas_teste, 3, arquivo)
    arquivo.close()

def medir_tempo_execucao(qtd_rotas, rotas, dispersao, num_caminhoes):
    tempos_execucao = []
    tempoMaior = []
    
    for i in range(10):  # Testar 10 vezes para calcular a média
        inicio = time.time()
        backtracking(rotas, num_caminhoes)
        fim = time.time()
        
        tempos_execucao.append(fim - inicio)
        
        print(f"{i} - Tempo da execução: {tempos_execucao[i]}")
        
        if tempos_execucao[i] >= 30:
            tempoMaior.append(tempos_execucao)
            
            print(f"Conjunto que ultrapassou: {rotas}")
            break
    tempo_medio = sum(tempos_execucao) / len(tempos_execucao)
    print(f"FINAL: {qtd_rotas}")
    if tempo_medio > 30.0:
        return False, rotas
    return True, []

def backtracking(rotas, num_caminhoes):
    print(f'----------------------- BACKTRACKING -----------------------\n')
    
    for rota in rotas:
        melhor_distribuicao, melhor_diferenca = distribuir_rotas_backtracking(rota, num_caminhoes)

        print("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:")
        for i, caminhao in enumerate(melhor_distribuicao):
            print(f"Caminhão {i + 1}: {caminhao}")
        print(f"Diferença mínima de quilometragem: {melhor_diferenca} km")



def divisaoconquista(rotas, num_caminhoes):
    print(f'------------------- DIVISÃO E CONQUISTA -------------------\n')
    for rota in rotas:
        distribuicao = distribuir_rotas_divisao_conquista(rota, num_caminhoes)

        print("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:")
        for i, caminhao in enumerate(distribuicao):
            print(f"Caminhão {i + 1}: {caminhao}")
        print(f"Diferença mínima de quilometragem: {diferenca_entre_caminhoes([sum(caminhao) for caminhao in distribuicao])} km")


def medir_tempo_prog_dinamica(qtd_rotas, rotas, num_caminhoes, arquivo):
    tempos_execucao = []

    for i in range(10):  # Testar 10 vezes para calcular a média
        inicio = time.time()
        programacaodinamica(rotas, num_caminhoes, arquivo)
        fim = time.time()
        
        tempos_execucao.append(fim - inicio)

    tempo_medio = sum(tempos_execucao) / len(tempos_execucao)
    arquivo.write(f"Tempo médio para o conjunto de tamanho {qtd_rotas} foi: {tempo_medio}\n")
    print(f"Tempo médio para o conjunto de tamanho {qtd_rotas} foi: {tempo_medio}")


def programacaodinamica(rotas, num_caminhoes, arquivo):
    arquivo.write(f'------------------- PROGRAMAÇÃO DINAMICA --------------------\n')
    print(f'------------------- PROGRAMAÇÃO DINAMICA --------------------\n')
    
    for rota in rotas:
        melhor_distribuicao = distribuir_rotas_dinamica(rota, num_caminhoes)

        arquivo.write("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:\n")
        print("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:")
        for i, caminhao in enumerate(melhor_distribuicao):
            arquivo.write(f"Caminhão {i + 1}: {caminhao} -- Quilometragem: {sum(caminhao)} km\n")
            print(f"Caminhão {i + 1}: {caminhao} -- Quilometragem: {sum(caminhao)} km")

if __name__ == "__main__":
    main()
