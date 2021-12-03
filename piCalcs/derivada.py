from sympy import *

q = symbols('q')


def funcao_custo(q):
    return 0.03*q**3 - 1.8*q**2 + 39*q


class Financeiro:
    def __init__(self):
        self.custos = funcao_custo(q)
        self.preco_venda = 21
        self.lucro = self.preco_venda*q - self.custos

    def raizes(self):
        derivada1 = self.lucro.diff(q)
        a = solve(derivada1, q)

        return a

    def calc_max(self):
        derivada2 = self.lucro.diff(q).diff(q)
        raizes_q = self.raizes()

        lista_val_raiz = {}

        val_min = []

        val_max = []

        for raiz in raizes_q:
            valor = derivada2.subs(q, raiz)

            lista_val_raiz[valor] = raiz

        for valor in lista_val_raiz.keys():
            if valor > 0:
                val_min.append(lista_val_raiz[valor])
            elif valor < 0:
                val_max.append(lista_val_raiz[valor])

        return val_max