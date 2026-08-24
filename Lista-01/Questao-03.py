#==================== Sistema de avaliação acadêmica =========================
notas = []
for nota in range(1, 4):
    nota_aluno = float(input(f"Digite a {nota}ª nota: "))
    notas.append(nota_aluno)
nota_1, nota_2, nota_3 = notas[0:3]

percent_freq = float(input("Digite o % de frequencia: "))
quant_atividades_entregues = int(input("Digite a quantidade de atividades entregues: "))
quant_total_de_atividades = int(input("Digite o quantidade total de atividades: "))

#TODO - Acredito que exista um erro de regra na questao: se o aluno tiver media: 8, frequencia: 76%, porcent de atividades: 53%
# ele nao pode ser aprovado com excelencia por conta da frequencia, aprovacao normal tambem nao por conta
# da percentagem de atividades entregues, nao pode ir pra recuperacao por conta da media e muito menos ser reprovado,
# como decidir essa situacao?

lista_info = []
def capturarInfo(info):
    if info not in lista_info:
        lista_info.append(info)

def mediaDeNotas() -> float:
    media = sum(notas) / len(notas)
    return media

def calcularPercentAtividadesEntregues() -> float:
    percent_atividades = (quant_atividades_entregues * 100) / quant_total_de_atividades
    return percent_atividades

def testarSeAprovadoComExecelencia() -> bool:
    media = mediaDeNotas() >= 9
    frequencia = percent_freq >= 90
    atividades = calcularPercentAtividadesEntregues() == 100.0

    if not media: capturarInfo("Media abaixo de 9.0 para Aprovacao com Excelencia.")
    if not frequencia: capturarInfo("Frequencia abaixo de 90% para Aprovacao com Excelencia.")
    if not atividades: capturarInfo("Todas as atividades deviam ser entregues para aprovacao com Excelencia.")

    if media and frequencia and atividades:
        return True
    else:
        return False

def testarSeAprovado() -> bool:
    media = mediaDeNotas() >= 7.0
    frequencia = percent_freq >= 75
    atividades = calcularPercentAtividadesEntregues() >= 70

    if not media: capturarInfo("Media abaixo de 7.0 para Aprovacao.")
    if not frequencia: capturarInfo("Frequencia abaixo de 75% para Aprovacao.")
    if not atividades: capturarInfo("Pelo menos 70% das atividades deviam ser entregues para Aprovacao.")

    if media and frequencia and atividades:
        return True
    else:
        return False

def testarSeRecupecacao() -> bool:
    media = mediaDeNotas() >= 5 and mediaDeNotas() <= 6.99
    frequencia = percent_freq >= 75

    if not media: capturarInfo("Sua media deve estar entre 5.0 e 7.0 para Recuperacao.")
    if not frequencia: capturarInfo("Sua frequencia deve ser pelo menos 75% para Recuperacao.")

    return media and frequencia

def analisarReprovacao() -> None:
    frequencia = percent_freq < 75
    media = mediaDeNotas() < 5
    if frequencia: capturarInfo("Frequencia abaixo do requerido (75%).")
    if media: capturarInfo("Media abaixo de 5.0.")
    return None

def exibirResultados(resultado):
    print(f"""
    ------------ Resultado Academico -------------
    Resultado final ------------------ {resultado}
    Media final ---------------------- {mediaDeNotas():.1f}
    Frequencia ----------------------- {percent_freq:.1f}%
    Atividades entregues ------------- {calcularPercentAtividadesEntregues():.1f}%
    """)
    if len(lista_info) > 0:
        print("---------- Mais Informacoes ---------")
        for x in lista_info:
            print(x)

if percent_freq >= 75 and mediaDeNotas() >= 5.0:
    if testarSeAprovadoComExecelencia():
        exibirResultados("Aprovado com Execelencia.")
    elif testarSeAprovado():
        exibirResultados("Aprovado.")
    elif testarSeRecupecacao():
        exibirResultados("Recuperacao.")
else:
    analisarReprovacao()
    exibirResultados("Reprovado.")


