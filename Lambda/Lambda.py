#Funções Lambda
print("\n===================\n")

dobrar_com_lambda = lambda n: n * 2

print("LAMBDA:", dobrar_com_lambda(10))

print("\n===================\n")
#Função Regular
def dobrar(n):
    return n * 2

print("REGULAR: ",dobrar(10))

print("\n===================\n")

def classificar_numero(n):
    if n < 0:
        return "NEGATIVO"
    elif n == 0:
        return "ZERO"
    else:
        return "POSITIVO"

print(classificar_numero(10))
print("\n===================\n")

#TENTATIVA DE LAMBDA PARA CLASSIFICAR NUMEROS
classificar_com_lambda = lambda n : "NEGATIVO" if n < 0 else ("ZERO" if n == 0 else "POSITIVO")

print(classificar_com_lambda(10))

