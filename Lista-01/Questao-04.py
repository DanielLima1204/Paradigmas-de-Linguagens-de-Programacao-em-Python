#============================ Cálculo de frete inteligente =======================

#TODO - Checar com o professor se o desconto deve ser aplicado ao valor inicial do frete, que segue a regra basica de peso e distancia,
# ou no valor do frete apos os adicionais.

def getTipoEntrega() -> str:
    while(True):
        opcao = input("Digite o tipo de entrega: 1 -- Normal, 2 -- Expressa, 3 -- Urgente: ")
        match opcao:
            case "1":
                return "normal"
            case "2":
                return "expressa"
            case "3":
                return "urgente"
            case _:
                print("Valor invalido, tente novamente.")

def getSeAssinante() -> bool:
    while (True):
        opcao = input("Cliente Assinante? 1 -- Para SIM, 2 -- Para Nao: ")
        match opcao:
            case "1":
                return True
            case "2":
                return False
            case _:
                print("Valor invalido, tente novamente.")

peso_encomenda = float(input("Digite o peso da encomenda: "))
distancia = float(input("Digite a distancia em KM: "))
tipo_entrega: str = getTipoEntrega()
cliente_assinante = getSeAssinante()
valor_compra = float(input("Digite o valor da compra: "))

list_info = list()
def coletarInfo(info: str):
    if info not in list_info:
        list_info.append(info)

def exibirInfo(valor_frete_incial, valor_frete_final):
    print(f"Valor Inicial Frete ------------ {valor_frete_incial:.2f}R$")
    print(f"Valor final Frete ------------ {valor_frete_final:.2f}R$")
    print("""--------- DESCRITIVOS DE ADICIONAIS E DESCONTOS -----------""")
    if len(list_info) > 0:
        for x in list_info:
            print(x)

def calcularFreteInicial() -> float:
    taxa_peso = calcularTaxaPorPeso()
    taxa_distancia = calcularTaxaPorDistancia()
    valor_inicial_frete = taxa_peso + taxa_distancia
    return valor_inicial_frete

#Calculos Taxas
def calcularTaxaPorPeso() -> float:
    if peso_encomenda > 30:
        taxa_peso = 80
        coletarInfo(f"Peso superior a 30Kg Taxa adicional de: {taxa_peso:.2f}R$")
    else:
        taxa_peso = peso_encomenda * 2.50
        coletarInfo(f"Peso inferior a 30Kg (Taxa = peso x 0,30 R$): {taxa_peso:.2f}R$")
    return taxa_peso

def calcularTaxaPorDistancia() -> float:
    if distancia > 500:
        taxa_distancia = 100
        coletarInfo(f"Distancia superior a 500Km taxa adicional de: {taxa_distancia:.2f}R$")
    else:
        taxa_distancia = distancia * 0.30
        coletarInfo(f"Distancia inferior a 500Km (taxa = distancia x 0,30R$) total: {taxa_distancia:.2f}R$")
    return taxa_distancia

#Calculos Adicionais
def calcularAddPorTipoEntrega() -> float:
    valor_frete_inicial = calcularFreteInicial()
    valor_adicional_entrega = 0.00
    if tipo_entrega == "normal":
        coletarInfo("Tipo de entrega Normal adicional de: 0.00 R$")
        return valor_adicional_entrega
    elif tipo_entrega == "expressa":
        valor_adicional_entrega = valor_frete_inicial * 0.30
        coletarInfo(f"Tipo de entrega Expressa adicional de 30%: {valor_adicional_entrega:.2f}R$")
        return valor_adicional_entrega
    elif tipo_entrega == "urgente":
        valor_adicional_entrega = valor_frete_inicial * 0.60
        coletarInfo(f"Tipo de entrega Urgente adicional de 60%: {valor_adicional_entrega:.2f}R$")
        return valor_adicional_entrega

def calcularDescontos() -> float:
    valor_frete_inicial = calcularFreteInicial()
    if cliente_assinante and valor_compra > 1000:
        desconto = valor_frete_inicial * 0.20
        coletarInfo(f"Assinante e Valor de compra acima de 1000 desconto de 20%: {desconto:.2f}")
        return desconto
    elif cliente_assinante:
        desconto = valor_frete_inicial * 0.15
        coletarInfo(f"Assinante, desconto de 15%: {desconto:.2f}")
        return desconto
    elif valor_compra > 1000:
        desconto = valor_frete_inicial * 0.10
        coletarInfo(f"Valor de compra acima de 1000 desconto de 10%: {desconto:.2f}")
        return desconto
    else:
        coletarInfo("Nenhum desconto aplicado, pois nao e Assinante e Valor da Compra e muito baixo.")
        return 0.00

def testarSeGratuito():
    if cliente_assinante and valor_compra >= 2000 and tipo_entrega == "normal" and peso_encomenda <= 10:
        coletarInfo("""
                -------- FRETE GRATIS -------
                Assinante --------------------- SIM
                Valor de Compra --------------- maior/igual 2000 R$
                Tipo de Entrega --------------- NORMAL
                Peso Encomenda ---------------- menor/igual 10 KG
        """)
        return True
    else:
        return False

#Calculo Preco Final
def calcularValorFinal():
    valor_frete_inicial = calcularFreteInicial()
    valor_frete_final = 0.00
    if testarSeGratuito():
        exibirInfo(valor_frete_inicial, valor_frete_final)
        return None
    else:
        taxa_peso = calcularTaxaPorPeso()
        taxa_distancia = calcularTaxaPorDistancia()
        adic_entrega = calcularAddPorTipoEntrega()
        descontos = calcularDescontos()
        valor_frete_final = (taxa_peso + taxa_distancia + adic_entrega) - descontos
        exibirInfo(valor_frete_inicial, valor_frete_final)
        return None

calcularValorFinal()