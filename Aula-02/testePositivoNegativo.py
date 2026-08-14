def testePositivoOuNegativo(numero: int) -> str:
    if numero != 0 and numero > 0:
        return f"O numero {numero} é positivo!"
    elif numero != 0 and numero < 0:
        return f"O numero {numero} é negativo!"
    else:
        return "O numero é zero!"

while(True):
    numero = int(input("Digite um numero: "))
    print(testePositivoOuNegativo(numero))