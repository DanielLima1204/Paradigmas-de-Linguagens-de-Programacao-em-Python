#===================== Cálculo completo de imposto de renda =============================

salario_bruto = float(input("Digite seu salario bruto: "))
qnt_dependentes = int(input("Digite a quantidade de dependentes: "))
valor_pg_previdencia = float(input("Digite o valor pago em Previdencia: "))
valor_pensao_alimt = float(input("Digite o valor de Pensao Alimenticia: "))

lista_info = []

#Funcoes para testes de regras
def testarSeDeducaoMaiorQueSalarioBruto(salario_bruto):
    deducao_dependetes = calcularDeducaoPorDepend(qnt_dependentes)
    if deducao_dependetes >= salario_bruto:
        return True
    else:
        return False

#Funcoes para calculos
def calcularDeducaoPorDepend(qnt_dependentes) -> int:
    valor_deducao = qnt_dependentes * 250
    return valor_deducao

def calcularBaseDeCalculo() -> float:
    if testarSeDeducaoMaiorQueSalarioBruto(salario_bruto):
        return 0.0
    else:
        base_de_calculo = salario_bruto - valor_pg_previdencia - valor_pensao_alimt - calcularDeducaoPorDepend(qnt_dependentes)
        return base_de_calculo

 #TODO Ver com professor a regra correta para o salario liquido
def calcularSalarioLiquido():
    salario_liquido = salario_bruto - valor_pg_previdencia - valor_pensao_alimt
    return salario_liquido

def calcularAliquota() -> float:
    base_calc = calcularBaseDeCalculo()
    if base_calc <= 2500:
        return 0.0
    else:
        if base_calc <= 3500:
            return 0.075
        elif base_calc <= 5000:
            return 0.15
        elif base_calc <= 7500:
            return 0.225
        else:
            return 0.275

def calcularImposto() -> float:
    base_calc = calcularBaseDeCalculo()
    aliquota = calcularAliquota()
    imposto = (base_calc * aliquota)
    return imposto

def exibirInfo():
    print(f"""
    --------- Sua Informacoes --------
    Salario Bruto ------------- {salario_bruto:.2f}R$
    Total de Deducoes --------- {calcularDeducaoPorDepend(qnt_dependentes) + valor_pensao_alimt + valor_pg_previdencia:.2f}R$
    Base de Calculo ----------- {calcularBaseDeCalculo():.2f}R$
    Aliquota ------------------ {calcularAliquota() * 100}%
    Imposto ------------------- {calcularImposto():.2f}R$
    Salario Liquido ----------- {calcularSalarioLiquido():.2f}R$    
    """)

exibirInfo()
