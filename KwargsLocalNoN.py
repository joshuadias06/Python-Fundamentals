
def exibir_informcoes(**kwargs):
    #Função que exibe informacões pessoais
    for key, value in kwargs.items():
        print(key + ":" + str(value))


exibir_informcoes(nome = "Joshua", idade = 21, cidade = "São Paulo", sexo = "Masculino")