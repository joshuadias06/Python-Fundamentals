"""#Incremento
from SomaImpares import soma_impares

for i in range(1, 11):
    print(i)

#Decremento
for j in range(10, 0, -1):
    print(j)

#Incremento 2 em 2
for k in range(1, 20, 2):
    print(k)
    """
#SOMA IMPARES COM FOR
soma_impares= 0

for cont in range(1, 10):
    if cont % 2 != 0:
        soma_impares += cont

    cont += 1
    print(soma_impares)