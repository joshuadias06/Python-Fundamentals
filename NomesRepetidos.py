list = ["Ana", "João", "Maria", "Ana", "Pedro", "João", "Carlos", "Maria"]
unique_list = []

for name in list:
    if name not in unique_list:
        unique_list.append(name)
        print(name)
