salario = float(input("Digite seu salario: "))
percenual = 5
valor_aumento = salario * 0.05

if salario <= 2000:
    # salario_aumentado = ((10 / 100) * salario) + salario
    percenual = 10
    valor_aumento = salario * 0.1

    salario_aumentado = valor_aumento + salario
    print(f"Aumento de: {percenual} %")
    print(f"Valor do aumento: {valor_aumento:.2f}")
    print(f"Seu novo salário é: {salario_aumentado:.2f}")