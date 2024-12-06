soma_pares = 0

for i in range(1, 11):
    if i % 2 == 0:
        soma_pares += i
    print("Contador:", i,"Soma Dos Pares:", soma_pares)


for j in range(0, 100, 2):
    if j % 2 == 0:
        soma_pares += j

print(f"Existem {j / 2} numeros pares de 1 a 100 e a soma deles é{soma_pares}")