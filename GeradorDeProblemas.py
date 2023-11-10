import random

class GeradorDeProblemas:
    aleatorio = random.Random(42)
    TAM_BASE = 13

    #  * Gerador de rotas aleatórias para testes de FPAA. Recebe como parâmetros a quantidade de rotas para um teste, 
    #  * o tamanho do conjunto de testes (ou seja, quantos conjuntos de rotas daquele tamanho serão gerados) e a dispersão. 
    #  * A dispersão deve ser dada em porcentagem e indica a diferença possível entre a menor rota e a maior rota. Supõe-se
    #  * que conjuntos com dispersões diferentes possam gerar resultados com características muito diferentes. Este método 
    #  * não está robusto contra nenhum tipo de erro de valores dos parâmetros. 
    #  * @param quantRotas A quantidade de rotas que será utilizada em um teste. Deve ser um número inteiro positivo preferencialmente maior que 5.
    #  * @param tamConjunto O tamanho do conjunto de testes, isto é, quantos conjuntos de rotas do tamanho acima serão gerados.
    #  * @param dispersao A dispersão do tamanho das rotas em %. Por exemplo, se a dipersão for 0.50 (50%), as rotas geradas estarão
    #  * entre 13 e 20. Uma dispersão de 1.0 (100%) gera conjuntos de rotas entre 13 e 26. 
    #  * @return Retorna uma lista de conjuntos de rotas. Cada conjunto de rotas é um vetor de números inteiros.


# tamConjunto => quantidade de caminhoes
# quantRotas => quantas rotas existem
# dispersao => O quão distante serão umas das outras
    def geracaoDeRotas(quantRotas, tamConjunto, dispersao):
        conjuntoDeTeste = []
        tam_max = int(GeradorDeProblemas.TAM_BASE * (1 + dispersao))

        for i in range(tamConjunto):
            rotas = [GeradorDeProblemas.aleatorio.randint(GeradorDeProblemas.TAM_BASE, tam_max) for _ in range(quantRotas)]
            conjuntoDeTeste.append(rotas)

        return conjuntoDeTeste
