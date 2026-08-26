#======================== Diagnóstico financeiro familiar ============================

todos_gastos = {
    "Moradia": 0.00,
    "Alimentacao": 0.00,
    "Transporte": 0.00,
    "Saude": 0.00,
    "Educacao": 0.00,
    "Lazer": 0.00,
    "Divida": 0.00
}

renda_mensal = float(input("Digite sua renda mensal: "))
for x in todos_gastos:
    gasto = float(input(f"Digite seu gasto com {x}: "))
    todos_gastos[x] = gasto

#Calculos
def calcularTotalDeDespesas() -> float:
    lista_gastos = []
    for valor in todos_gastos.values():
        lista_gastos.append(valor)
    total_despesas = sum(lista_gastos)
    return total_despesas

def calcularSaldoMensal() -> float:
    despesas = calcularTotalDeDespesas()
    saldo_mensal = renda_mensal - despesas
    return saldo_mensal

def calcularPorcentRendaComprometida() -> float:
    gastos_fixos = calcularTotalDeDespesas()
    porcentagem = (gastos_fixos * 100) / renda_mensal
    return porcentagem

def calcularPorcentDivida() -> float:
    divida = todos_gastos["Divida"]
    porcentagem = (divida * 100) / renda_mensal
    return porcentagem

def testarPorcentSaldoNegativo() -> bool:
    saldo = calcularSaldoMensal()
    if saldo < 0:
        if abs(saldo) >= renda_mensal * 0.20:
            return True
        else:
            return False
    else:
        return False

#Testes
def testarSeSaudavel() -> bool:
    comprometimento = calcularPorcentRendaComprometida()
    dividas = calcularPorcentDivida()
    if comprometimento <= 70 and dividas <= 20:
        return True
    else:
        return False

def testarSeAtencao() -> bool:
    dividas = calcularPorcentDivida()
    saldo_negativo_superior_renda = testarPorcentSaldoNegativo()
    comprometimento = calcularPorcentRendaComprometida()
    if (comprometimento > 70 and comprometimento <= 85) and dividas < 35 and not saldo_negativo_superior_renda:
        return True
    else:
        return False

def testarSeCritica() -> bool:
    comprometimento = calcularPorcentRendaComprometida()
    dividas = calcularPorcentDivida()
    saldo_negativo_superior_renda = testarPorcentSaldoNegativo()
    if (comprometimento > 85 or dividas > 35) and not saldo_negativo_superior_renda:
        return True
    else:
        return False

def testarInsolvencia() -> bool:
    despesas_maior_que_renda = calcularTotalDeDespesas() > renda_mensal
    if despesas_maior_que_renda and testarPorcentSaldoNegativo():
        return True
    else:
        return False

def apresentarRecomendacoes(resultado: str):
    print(f"""
    ------------- SUA SAUDE FINANCEIRA -------------
    Suas despesas: ---------------------- {calcularTotalDeDespesas():.2f}R$
    Seu Saldo Mensal: ------------------- {calcularSaldoMensal():.2f}R$
    Percentual de Renda Comprometida: --- {calcularPorcentRendaComprometida():.2f}%
    Percentual gasto em Dividas: -------- {calcularPorcentDivida():.2f}%
    O seu Diagnostico é: ---------------- {resultado.upper()}
""")
    match resultado:
        case "saudavel":
            print("""
            Recomendacao: Mantenha o controle financeiro, preserve uma reserva de emergência e
                evite assumir novas dívidas desnecessárias.""")
        case "atencao":
            print("""
            Recomendacao: Revise seus gastos e reduza despesas não essenciais para evitar 
                que o comprometimento da renda continue aumentando.
            """)
        case "critica":
            print("""
                Recomendacao: Priorize a redução de dívidas e corte gastos não essenciais. 
                Evite novos empréstimos até recuperar o equilíbrio financeiro.
            """)
        case "insolvencia":
            print("""
                Recomendacao: Suspenda novos gastos e dívidas, reduza imediatamente as despesas e busque renegociar as dívidas 
                existentes para recuperar o equilíbrio financeiro.
            """)

def gerarDiagnostico():
    if testarSeSaudavel():
        apresentarRecomendacoes("saudavel")
    elif testarSeAtencao():
        apresentarRecomendacoes("atencao")
    elif testarSeCritica():
        apresentarRecomendacoes("critica")
    elif testarInsolvencia():
        apresentarRecomendacoes("isolvencia")
    else:
        pass

gerarDiagnostico()

