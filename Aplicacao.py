import time
from backtracking.Backtracking import distribuir_rotas_backtracking
from GeradorDeProblemas import GeradorDeProblemas
from divisaoconquista.Divisao_Conquista import distribuir_rotas_divisao_conquista
from divisaoconquista.Divisao_Conquista import diferenca_entre_caminhoes
from divisaoconquista.Divisao_Conquista import divide_rotas

def main():
    qtd_rotas = 6
    qtd_conjunto = 3
    dispersao = 85
    whileTime = True
    
    while whileTime:
        conjunto = GeradorDeProblemas.geracaoDeRotas(qtd_rotas, qtd_conjunto, dispersao)
        whileTime = medir_tempo_execucao(qtd_rotas, conjunto, dispersao, 3)

        qtd_rotas += 1   

def backtracking(rotas, num_caminhoes):
    print(f'----------------------- BACKTRACKING -----------------------\n')
    
    for rota in rotas:
        melhor_distribuicao, melhor_diferenca = distribuir_rotas_backtracking(rota, num_caminhoes)

        print("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:")
        for i, caminhao in enumerate(melhor_distribuicao):
            print(f"Caminhão {i + 1}: {caminhao}")
        print(f"Diferença mínima de quilometragem: {melhor_diferenca} km")

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
        return False
    return True

def divisaoconquista(rotas, num_caminhoes, tempo_limite):
    print(f'------------------- DIVISÃO E CONQUISTA -------------------\n')
    for rota in rotas:
        distribuicao = distribuir_rotas_divisao_conquista(rota, num_caminhoes)

        print("Distribuição encontrada para minimizar a diferença de quilometragem entre os caminhões:")
        for i, caminhao in enumerate(distribuicao):
            print(f"Caminhão {i + 1}: {caminhao}")
        print(f"Diferença mínima de quilometragem: {diferenca_entre_caminhoes([sum(caminhao) for caminhao in distribuicao])} km")

def medir_divisaoconquista(rotas, num_caminhoes, tempo_limite):
    qtd_rotas = 6
    
    while True:
        tempos_execucao = []
        
        for _ in range(10):
            rotas_teste = GeradorDeProblemas.geracaoDeRotas(qtd_rotas, num_caminhoes, dispersao=0.5)
            
            inicio = time.time()
            distribuicao = distribuir_rotas_divisao_conquista(rotas_teste, num_caminhoes)
            fim = time.time()
            
            tempo_execucao = fim - inicio
            tempos_execucao.append(tempo_execucao)

            # Exibe a distribuição de rotas após cada execução
            print(f"Distribuição de rotas para {num_caminhoes} caminhões:")
            for idx, caminhao in enumerate(distribuicao):
                print(f"Caminhão {idx + 1}: {caminhao}")

        tempo_medio = sum(tempos_execucao) / len(tempos_execucao)
        print(f"Tamanho {qtd_rotas}: Tempo médio de execução: {tempo_medio:.6f} segundos")

        if tempo_medio > tempo_limite:
            break

        qtd_rotas += 1

if __name__ == "__main__":
    # Conjuntos de rotas fornecidos
    rotas1 = [40, 36, 38, 29, 32, 28, 31, 35, 31, 30, 32, 30, 29, 39, 35, 38, 39, 35, 32, 38, 32, 33, 29, 33, 29, 39, 28]
    rotas2 = [32, 51, 32, 43, 42, 30, 42, 51, 43, 51, 29, 25, 27, 32, 29, 55, 43, 29, 32, 44, 55, 29, 53, 30, 24, 27]

    # Adicione os conjuntos de rotas à lista de testes
    rotas_teste = [rotas1, rotas2]

    main()
    divisaoconquista(rotas_teste, 3, 30)  # Chamada da função de divisão e conquista
    medir_divisaoconquista(rotas_teste, 3, 30)  # Chamada da função para medir tempo na divisão e conquista
