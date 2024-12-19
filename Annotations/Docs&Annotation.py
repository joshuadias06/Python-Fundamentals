"""
Documentações e Anotações de Funções

1. Docstrings
-- O que uma função faz e o que retorna.
"""

#Exemplo
def somar(a,b):
    """PEGA A VARIAVEL a E SOMA COM A VARIVEL b"""
    return a+b

print(somar(3,4))
print(somar.__doc__)

print("=========================================")

#2. Anotações de Tipo (Type Hints)

def multiplicar(a:int, b:int) -> int:

    return a * b

print(multiplicar(3,4))
print(multiplicar.__annotations__)