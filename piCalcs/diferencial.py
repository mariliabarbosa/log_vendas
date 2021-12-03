from sympy import *

q = symbols('q')


def funcaoCusto(q):
    return 0.03*q**3 - 1.8*q**2 + 39*q


class Financeiro:
    def __init__(self):
        self.custos = funcaoCusto(q)
        self.precoVenda = 21
        self.lucro = self.precoVenda*q - self.custos

    def raizes(self):
        diferencial1 = self.lucro.diff(q)
        a = solve(diferencial1, q)

        return a

    def calcMax(self):
        diferencial2 = self.lucro.diff(q).diff(q)
        raizesQ = self.raizes()

        listaValRaiz = {}

        valMin = []

        valMax = []

        for raiz in raizesQ:
            valor = diferencial2.subs(q, raiz)

            listaValRaiz[valor] = raiz

        for valor in listaValRaiz.keys():
            if valor > 0:
                valMin.append(listaValRaiz[valor])
            elif valor < 0:
                valMax.append(listaValRaiz[valor])

        return valMax