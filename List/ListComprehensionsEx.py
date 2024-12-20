cubo = [x**3 for x in range(10)]
print(cubo)

divisiveis_por3 = [i for i in range(1, 20) if i % 3 == 0]
print(divisiveis_por3)

frutas = ["maca", "banana", "manga", "uva", "abacaxi", "laranja"]
frutas_maiores5 = [fruta for fruta in frutas if len(fruta) >= 5]
print(frutas_maiores5)

notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]
nota_corte = [nota for nota in notas if nota >= 75]
print(nota_corte)