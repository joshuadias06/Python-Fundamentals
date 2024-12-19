#Riscos e limitações das recursão em Python.

def recursao_infinita(n):
    print(n)

    recursao_infinita(n + 1)

recursao_infinita(1)
#LOOP INFINITO - RecursionError - apenas 1000 chamadas recursivas