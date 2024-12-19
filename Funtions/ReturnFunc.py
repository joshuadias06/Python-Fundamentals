def nivel_saudacao(nivel):
    def saudacao_basica():
        return "Oi!"

    def saudacao_avancada():
        return "Ola! Como voce esta?"

    if nivel == "basico":
        return saudacao_basica
    else:
        return saudacao_avancada

cumprimento = nivel_saudacao("basico")
print(cumprimento())