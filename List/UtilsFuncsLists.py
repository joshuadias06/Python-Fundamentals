numeros = [i*6 for i in range(1, 10)]
print(numeros)

soma = sum(numeros)
print(soma)
tamanho = len(numeros)
print(tamanho)
maior = max(numeros)
print(maior)
minimo = min(numeros)
print(minimo)

pesos = [58.5, 63.2, 71.3, 69.4, 68.2]
soma_pesos = sum(pesos)
media_pesos = soma_pesos / len(pesos)
print(f"A Soma de todos os pesos é: {soma_pesos} e a média de pesos é: {media_pesos}")