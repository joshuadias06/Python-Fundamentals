#Fora de qualquer funcao
var_global = "Eu sou uma variavel global"

def funcao_exemplo():
    global var_global

    #Dentro do escopo da funcao
    var_local = "Eu sou um variavel local"
    print(var_local)
    print(var_global)

    var_global = "oi"
    print(var_global)

funcao_exemplo()