import math


def raizQuadrada(raiz):
    raiz = math.sqrt(raiz)

    return raiz

raizQ = float(input("Digite o valor de raiz quadrada: "))
resultado = raizQuadrada(raizQ)
print(resultado)

