"""
Autores: Daniel Lima -- Matricula: 202604118294 - Digitador
	 Frederico Almeida -- Matricula: 202602155401 - Apoiador
	 Luiz Ricardo da Silva Oliveira -- Matricula: 202601564293 - Apoiador
"""
#Sistema de Classificação de Crédito

idade = int(input("Digite sua idade: "))
salario_mensal = float(input("Digite seu salario mensal: "))
divida_atual = float(input("Digite sua duvida atual: "))
tempo_do_emprego_em_meses = int(input("Digite seu tempo de emprego em meses: "))
valor_solicitado = int(input("Qual valor de credito você deseja: "))
numero_parcelas = int(input("Em quantas vezes deseja parcelar: "))

lista_reprov = list()

#Funcoes de calculos uteis
def calcularPorcentCompromAtual() -> float:
    return (divida_atual / salario_mensal) * 100

def calcularPorcentCompromNovo() -> float:
    return ((divida_atual + calcularValorParcelas()) / salario_mensal) * 100

def calcularPorcentagemSalario(porcent) -> float:
    return (porcent / 100) * salario_mensal

def calcularValorParcelas() -> float:
    valor_das_parcelas = valor_solicitado / numero_parcelas
    return valor_das_parcelas

#Funcao para agrupar motivos para reprovacao
def capturarMotivosReprov(motivo) -> None:
    if motivo not in lista_reprov:
        lista_reprov.append(motivo)

#Funcoes de testes das regras de negocio
def testarIdade() -> bool:
    idade_aprov = idade >= 21 and idade <= 65
    if idade_aprov:
        return True
    else:
        capturarMotivosReprov("Idade menor que o especificado (De 21 a 65 anos)")
        return False

def testarSalario() -> bool:
    salario_aprov = salario_mensal >= 2500
    if not salario_aprov: capturarMotivosReprov("Salario menor que o especificado (no minimo 2.500,00 R$)")
    return salario_aprov

def testarValorParcela(porcent_maxima) -> bool:
    if calcularValorParcelas() <= calcularPorcentagemSalario(porcent_maxima):
        return True
    else:
        capturarMotivosReprov("Valor da Parcela execede 25% do salario")
        return False

def testarComprometimentoAtual() -> bool:
    comprometimento = calcularPorcentCompromAtual() <= 30
    if comprometimento:
        return True
    else:
        capturarMotivosReprov("Comprometimento Atual maior que 30% do seu Salario")
        return False

def testarComprometimentoNovo() -> bool:
    comp_novo = (divida_atual + calcularValorParcelas()) <= calcularPorcentagemSalario(50)
    if comp_novo:
        return True
    else:
        capturarMotivosReprov("Novo comprometimento maior que 50% do seu Salario")
        return False

def testarTempoDeEmprego(tempo_minimo):
    if tempo_do_emprego_em_meses >= tempo_minimo:
        return True
    else:
        capturarMotivosReprov("Tempo de emprego menor que o especificado")
        return False

#Funcoes de Analise
def testarSeAprovado() -> bool:
    idade_aprovada = testarIdade()
    salario_aprovado = testarSalario()
    tempo_emprego = testarTempoDeEmprego(12)
    comp_atual = testarComprometimentoAtual()
    valor_parcela = testarValorParcela(25)

    if idade_aprovada and salario_aprovado and tempo_emprego and comp_atual and valor_parcela:
        return True
    else:
        return False

def testarComRestricoes() -> bool:
    idade_aprov = testarIdade()
    salario_aprov = testarSalario()
    tempo_emprego = testarTempoDeEmprego(6)
    novo_comprometimento = testarComprometimentoNovo()

    if idade_aprov and salario_aprov and tempo_emprego and novo_comprometimento:
        return True
    else:
        return False

#Funcao de exibicao
def exibirInfo(resultado):
    print(f"""
        Valor da parcela -------------------------- {calcularValorParcelas():.2f}
        Atual Percentual de Comprometimento ------- {calcularPorcentCompromAtual():.2f}%
        Novo Percentual de Comprometimento -------- {calcularPorcentCompromNovo():.2f}%
        Resultado da Analise ----------------------- {resultado}
    """)
    if len(lista_reprov) > 0:
        print("----------- Motivos da Reprovacao/Restricao ------------- ")
        for x in lista_reprov:
            print(x)

if testarSeAprovado():
    exibirInfo("Credito Aprovado!")
else:
    if testarComRestricoes():
        exibirInfo("Credito com Algumas restricoes")
    else:
        exibirInfo("Credito Reprovado!")