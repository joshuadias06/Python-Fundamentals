nomes = ["Ana", "João", "Maria", "Ana", "Pedro", "João", "Carlos", "Maria"]
unique_list = []

for i in nomes:
    if i not in unique_list:
        unique_list.append(i)
        print(i)
