matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento = matriz[1][2]
print(elemento)

soma = 0

for linha in matriz:
    for coluna in linha:
        soma += coluna

print(soma)

for linha in matriz:
    for coluna in linha:
        print(coluna, end=" ")
    print()