import random
import math

class GeradorDeProblemas:
    aleatorio = random.Random(42)
    TAM_BASE = 13

    def geracaoDeRotas(quantRotas, tamConjunto, dispersao):
        conjuntoDeTeste = []
        tam_max = int(math.ceil(GeradorDeProblemas.TAM_BASE * (1 + dispersao)))

        for i in range(tamConjunto):
            rotas = [GeradorDeProblemas.aleatorio.randint(GeradorDeProblemas.TAM_BASE, tam_max) for _ in range(quantRotas)]
            conjuntoDeTeste.append(rotas)
        return conjuntoDeTeste
