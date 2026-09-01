while True:
    try:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        divicao = num1 / num2
        print(f"Resultado: {divicao}")
    except ZeroDivisionError:
        print("Nao pode ser dividido por zero")
    except ValueError:
        print("Digite um valor valido")
    except:
        print("Algo deu erro digite novamente")
