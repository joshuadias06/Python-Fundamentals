"""
Funções Internas - built-in functions
Já vem embutidas na linguagem Python
-print(),len(),input(),etc.
-int(),float(),str(),etc.
"""

#Recursão

def contar_regressivamente(n):
    if n > 0:
        print(n)

        contar_regressivamente(n-1)

contar_regressivamente(5)