def saudacao_nome(nome):
    return f"Olá, {nome}"

def cumprimentar(funcao, nome):
    return funcao(nome)

print(cumprimentar(saudacao_nome, "Joshua"))
