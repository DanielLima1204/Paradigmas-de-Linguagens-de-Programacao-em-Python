def testePositivoOuNegativo(numero: int) -> str:
    if numero != 0 and numero > 0:
        return f"O numero {numero} é positivo!"
    elif numero != 0 and numero < 0:
        return f"O numero {numero} é negativo!"
    else:
        return "O numero é zero!"
def testeSeParOuImpar(numero: int) -> str:
    if numero % 2 == 0:
        return f"O numero {numero} é par"
    else:
        return f"O numero {numero} é impar!"

while(True):
    numero = int(input("Digite um numero: "))
    print(testePositivoOuNegativo(numero))
    print(testeSeParOuImpar(numero))

