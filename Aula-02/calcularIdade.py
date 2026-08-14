def calcularIdade() -> str:
    nome_pessoa = str(input("Digite seu nome: "))
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = ano_atual - ano_nascimento
    resultado = f"{nome_pessoa.capitalize()} sua Idade aproximada é: {idade} anos"
    return resultado

print(calcularIdade())