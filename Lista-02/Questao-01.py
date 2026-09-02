from datetime import datetime

senha_user = str(1234)
saldo_user = 1000
operacoes_user = list()
qnt_tentativas = 3

def registrarOperacoes(operacao: dict):
    operacoes_user.append(operacao)

def contabilizarOperacoes():
    if len(operacoes_user) > 0:
        qnt_saques = 0
        qnt_depositos = 0
        valor_total_saques = 0
        valor_total_depositos = 0
        for op in operacoes_user:
            if op["Tipo"] == "Saque":
                qnt_saques += 1
                valor_total_saques += op["Valor"]
            if op["Tipo"] == "Deposito":
                qnt_depositos += 1
                valor_total_depositos += op["Valor"]
        print(f"""
        ----------- CONTABILIZACAO DE OPERACOES --------------
        SAQUES ---------------------------------- {qnt_saques}
        VALOR TOTAL SACADO ---------------------- {valor_total_saques:.2f} R$
        DEPOSITOS ------------------------------- {qnt_depositos}
        VALOR TOTAL DEPOSITADO ------------------ {valor_total_depositos:.2f} R$
        SALDO ATUAL ----------------------------- {saldo_user} R$
        """)
    else:
        pass

def exibirOperacoes():
    if len(operacoes_user) > 0:
        print("""
        -------------- OPERACOES REALIZADAS ----------------
        """)
        for op in operacoes_user:
            for key, value in op.items():
                print(f"{key} -------------- {value}")
            print("----------------------------------------------------------------")
        contabilizarOperacoes()
    else:
        print("Ainda nao foi realizada nenhuma transacao.")

def consultarSaldo():
    print(f"""
    -------- CONSULTA DE SALDO -------
    SALDO ATUAL ---------------- {saldo_user:.2f}R$
    """)

def realizarDeposito(saldo_user) -> float:
    while True:
        valor = float(input("Digite o valor para Deposito: "))
        if valor > 0:
            novo_saldo = saldo_user + valor
            print(f"Deposito Realizado com Sucesso seu novo Saldo e: {novo_saldo:.2f} R$")
            operacao = {"Tipo": "Deposito", "Valor": valor, "Saldo Anterior": saldo_user, "Novo Saldo": novo_saldo, "Data e Hora": datetime.now()}
            registrarOperacoes(operacao)
            return novo_saldo
        else:
            print("O Valor para Deposito dever ser maior que 0.")

def realizarSaque(saldo: float):
    while True:
        valor = float(input("Digite um valor para Saque: "))
        saldo_maior_que_zero = saldo > 0
        valor_maior_que_zero = valor > 0
        saldo_relativo_valor = saldo >= valor
        if not saldo_maior_que_zero:
            print("Seu saldo no momento e 0.")
            return 0
        if not valor_maior_que_zero:
            print("O valor de Saque deve ser maior que 0.")
            continue
        if not saldo_relativo_valor:
            print("O seu valor de Saque deve ser menor ou igual ao valor do seu Saldo.")
            continue
        else:
            novo_saldo = saldo - valor
            print(f"Operacao realizada com sucesso seu novo saldo e: {novo_saldo:.2f}")
            operacao = {"Tipo": "Saque", "Valor": valor, "Saldo Anterior": saldo_user, "Novo Saldo": novo_saldo,
                        "Data e Hora": datetime.now()}
            registrarOperacoes(operacao)
            return novo_saldo

def menuGrafico():
    print("""
        ------------- BEM-VINDO AO DANIEL'S BANK --------------
        ESCOLHA UMA DAS OPCOES:
        1 ------------------------------------- CONSULTAR SALDO
        2 ----------------------------------- REALIZAR DEPOSITO
        3 -------------------------------------- REALIZAR SAQUE
        4 ----------------------------------- EXIBIR TRANSACOES
        5 ------------------------------------ ENCERRAR SERVICO
                       O QUE DESEJA FAZER HOJE? 
    """)

def menuOpcoes():
    while True:
        menuGrafico()
        global saldo_user
        opcao_user = input("DIGITE UMA OPCAO: ")
        match opcao_user:
            case '1':
                consultarSaldo()
                continue
            case '2':
                saldo_user = realizarDeposito(saldo_user)
                continue
            case '3':
                saldo_user = realizarSaque(saldo_user)
                continue
            case '4':
                exibirOperacoes()
                continue
            case '5':
                exibirOperacoes()
                print("Finalizando Sistema, Obrigado por sua presenca.")
                return 5
            case _:
                print("Digite um valor dentro das opcoes validas!")

while True:
    senha_digitada = input("Digite sua senha: ")
    if qnt_tentativas > 0:
        if senha_digitada != senha_user:
            print(f"Senha incorreta lhe restam {qnt_tentativas} tentativas")
            qnt_tentativas -= 1
        else:
            print("----- LOGIN EFETUADO COM SUCESSO ----------")
            menuOpcoes()
            break
    else:
        print("Execesso de tentativas invalidas programa encerrado!")
        break