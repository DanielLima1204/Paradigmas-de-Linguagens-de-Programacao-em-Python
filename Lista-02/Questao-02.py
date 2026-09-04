from random import random
numero_secreto = int(random() * 100) + 1
numero_tentativas = 0

def jogar(qnt_tentativas):
    numero_tentativas = qnt_tentativas
    while True:
        if numero_tentativas > 0:
            tentativa = int(input("Chute um numero: "))
            if tentativa > 100 or tentativa < 1:
                print("Digite um valor entre 0 e 100")
                continue
            elif tentativa > numero_secreto:
                print("Seu chute foi maior que o numero secreto!")
                numero_tentativas -= 1
                continue
            elif tentativa < numero_secreto:
                print("Seu chute foi menor que o numero secreto!")
                numero_tentativas -= 1
                continue
            elif tentativa == numero_secreto:
                numero_tentativas -= 1
                print(""" -------- VITORIA --------""")
                print(f"Tentativas utilizadas: {qnt_tentativas - numero_tentativas}")
                print(f"Sua pontuacao foi: {(qnt_tentativas - (qnt_tentativas - numero_tentativas)) * 100}")
                break

        else:
             print("Numero de tentativas esgotado!")
             print("Voce Perdeu")
             break

while True:
    nivel = input("Selecione um nivel: 1 - Facil, 2 - Medio e 3 - Dificil: ")
    match nivel:
        case '1':
            print("Selecionado Nivel Facil, Voce possui 10 tentativas.")
            jogar(10)
            break
        case '2':
            print("Selecionado Nivel Medio, Voce possui 7 tentativas.")
            jogar(7)
            break
        case '3':
            print("Selecionado Nivel Dificil, Voce possui 5 tentativas.")
            jogar(5)
            break
        case _:
            print("Digite uma das 3 opcoes validas!")

