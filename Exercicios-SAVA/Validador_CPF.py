#Escreva uma função que busca recursivamente o maior elemento em uma lista de números inteiros.
# ==================================== Validador de CPF =====================================

cpf = str(input("Digite seu CPF (Apenas Numeros): "))
#TODO Limpar espacos e remover caracteres especiais
def validarFormatoCPF(cpf):
    cpf_limpo = cpf.strip().translate(str.maketrans("", "", "-_.*@#!%&$?(){}[] =+/"))
    repetido = len(set(cpf_limpo)) == 1
    if repetido:
        return False
    else:
        return cpf_limpo

def calcularPrimeiroDigito(cpf_limpo):
    multiplicadores = [2,3,4,5,6,7,8,9,10]
    for _ in range(len(cpf_limpo) - 2):
        pass

