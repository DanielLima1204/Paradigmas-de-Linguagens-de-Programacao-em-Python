num1 = int(input("Digite o 1º numero: "))
num2 = int(input("Digite o 2º numero: "))
maior = 0
if num1 > num2:
    maior = num1
    print(f"O maior numero é {maior}!")
elif num2 > num1:
    maior = num2
    print(f"O maior numero é {maior}!")
else:
    print("Os numeros sao iguais!")