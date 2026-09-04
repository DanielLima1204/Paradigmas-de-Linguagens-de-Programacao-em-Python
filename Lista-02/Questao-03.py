estoque = 100
estoque_minimo = 1
total_entradas = 500
total_saidas = 20
movimentacoes = list()
estoque_inicial = (total_entradas - total_saidas) - estoque

def registrarMovimentacoes(movimentacao: dict):
    global total_entradas
    global total_saidas
    if movimentacao["Tipo"] == "Entrada": total_entradas += movimentacao["Quantidade"]
    if movimentacao["Tipo"] == "Saida": total_entradas += movimentacao["Quantidade"]
    movimentacoes.append(movimentacao)

def exibirInformacoes():
    if len(movimentacoes) > 0:
       pass

def consultarEstoque():
    print(f"--------- CONSULTA DE SALDO ATUAL DO ESTOQUE -----------")
    print(f"SALDO ATUAL ------------------------- {estoque} unidades")

def entradaMercadoria():
    global estoque
    while True:
        entrada = int(input("Digite a quantidade desejada: "))
        if entrada < 0:
            print("Os valores de entrada devem ser maior que zero!")
            continue
        else:
            estoque += entrada
            print(f"Entrada de {entrada} no estoque novo saldo de {estoque} itens.")
            movimentacao = {"Tipo": "Entrada", "Quantidade": entrada}
            registrarMovimentacoes(movimentacao)

def saidaMercadoria():
    global estoque
    while True:
        saida = int(input("Digite a quantidade que desaja retirar: "))
        if saida > estoque:
            print("A quantidade que deseja retirar e maior que a contida no estoque!")
            continue
        elif saida <= 0:
            print("A quantidade para retirada deve ser maior que zero!")
            continue
        else:
            estoque -= saida
            print(f"Entrada de {saida} no estoque novo saldo de {estoque} itens.")
            movimentacao = {"Tipo": "Saida", "Quantidade": saida}
            registrarMovimentacoes(movimentacao)

def definirEstoqueMinimo():
    global estoque_minimo
    while True:
        valor_estoque_minimo = int(input("Digite o valor para estoque minimo: "))
        if valor_estoque_minimo < 0:
            print("O valor para estoque minimo deve ser maior que zero.")
            continue
        else:
            estoque_minimo = valor_estoque_minimo
            print(f"Valor de estoque minimo definido para: {estoque_minimo}")

def exibirAlerta():
    if estoque >= estoque_minimo:
        print("SEU ESTOQUE ESTA NO MINIMO! POR FAVOR REPONHA OS ITENS!")

while True:
    opcao = input("""
    -------------- CONTROLE DE ESTOQUE --------------
        1 - Entrada de mercadoria
        2 - Saída de mercadoria
        3 - Consultar estoque
        4 - Definir estoque mínimo
        5 - Encerrar
    -------------------------------------------------    
    DIGITE UMA DAS OPCOES: """)
    match opcao:
        case '1':
            pass
        case '2':
            pass
        case '3':
            consultarEstoque()
            continue
        case '4':
            pass
        case '5':
            break
        case _:
            print("Digite uma das opcoes validas!")
            continue
