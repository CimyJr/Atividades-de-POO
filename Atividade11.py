import Atividade3


class Test:
    def test():
        p = Atividade3.Ponto(1, 1)
        print(p.qualQuadrante())
        quadrado = Atividade3.Quadrilatero(5, 4)
        print(quadrado.contidoEmQ(p))


Test.test()