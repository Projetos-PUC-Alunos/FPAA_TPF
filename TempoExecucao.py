import sys
import time

from Aplicacao import backtracking


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