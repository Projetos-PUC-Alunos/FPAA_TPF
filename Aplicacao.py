import time
from backtracking.Backtracking import distribuir_rotas_backtracking
from GeradorDeProblemas import GeradorDeProblemas

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


if __name__ == "__main__":
    main()