"""
Autores: Daniel Lima -- Matricula: 202604118294 - Digitador
	 Frederico Almeida -- Matricula: 202602155401 - Apoiador
	 Luiz Ricardo da Silva Oliveira -- Matricula: 202601564293 - Apoiador
"""


#Sistema de Classificação de Crédito

idade = int(input("Digite sua idade: "))
salario_mensal = float(input("Digite seu salario mensal: "))
valor_da_divida_atual = float(input("Digite sua duvida atual: "))
tempo_do_emprego_em_meses = int(input("Digite seu tempo de emprego em meses: "))
valor_solicitado = int(input("Qual valor de credito você deseja: "))
numero_parcelas = int(input("Em quantas vezes deseja parcelar: "))
#calculos
comprometimento = (valor_da_divida_atual / salario_mensal) * 100
print(comprometimento)
valor_da_parcela = valor_solicitado / numero_parcelas
resultado = False
if idade >= 21 and idade <= 65 and salario_mensal >= 2500 and tempo_do_emprego_em_meses >= 12 and comprometimento <= 30 and valor_da_parcela <= (salario_mensal * (25 / 100)):
    print("Credito aprovado!")
elif idade >= 21 and salario_mensal >= 2500 and tempo_do_emprego_em_meses >= 6 and ((valor_da_divida_atual / salario_mensal) + valor_da_parcela < salario_mensal / 2):
    print("Credito aprovado com restrições")
else:
    print("Reprovado!")
    print(f"""
    Valor Parcela: {valor_da_parcela:.2f}
    Percetual atual de comprometimento: {comprometimento:.2f}
    Novo percentual de comprometimento: {valor_solicitado / numero_parcelas:.2f}
    Resultado: Reprovado.
    Motivo: Nao esta apto


""")


