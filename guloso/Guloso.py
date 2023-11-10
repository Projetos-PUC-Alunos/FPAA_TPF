def distribuir_rotas_guloso_ord(rotas, num_caminhoes):
    rotas_ordenadas = sorted(rotas, reverse=True)
    
    caminhoes = [[] for _ in range(num_caminhoes)]
    
    for rota in rotas_ordenadas:
        caminhao_mais_leve = min(caminhoes, key=sum)
        caminhao_mais_leve.append(rota)
    
    quilometragens = [sum(caminhao) for caminhao in caminhoes]
    diferenca = max(quilometragens) - min(quilometragens)
    
    return caminhoes, diferenca

def distribuir_rotas_guloso(rotas, num_caminhoes):
    
    caminhoes = [[] for _ in range(num_caminhoes)]
    
    for rota in rotas:
        caminhao_mais_leve = min(caminhoes, key=sum)
        caminhao_mais_leve.append(rota)
    
    quilometragens = [sum(caminhao) for caminhao in caminhoes]
    diferenca = max(quilometragens) - min(quilometragens)
    
    return caminhoes, diferenca