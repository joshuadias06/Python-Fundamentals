#cidade ="Desconhecida" = ARGUMENTO DEFAULT
def exibir_informacoes(nome, idade, cidade ="Desconhecida"):

    print("===================")
    print("Nome: ", nome)
    print("Idade: ", idade)
    print("Cidade: ", cidade)

exibir_informacoes("João", 25, "São Paulo")
exibir_informacoes("Maria", 35)