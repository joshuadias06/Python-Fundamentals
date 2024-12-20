#Listas de LIstas = Matrizes

matriz = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
]

print(matriz[1][2])
print(matriz[1][1])

elemento = matriz[1][1]
print(elemento)

cont = 0

for linha in matriz:
    for coluna in linha:
        cont += 1
        print(f"ELEMENTO {cont}: {coluna}")


#4 Calc Transposta

transposta = []

for i in range(len(matriz[0])):
    linha_temp = []
    for j in range(len(matriz)):
        linha_temp.append(matriz[j][i])

    transposta.append(linha_temp)

print(transposta)