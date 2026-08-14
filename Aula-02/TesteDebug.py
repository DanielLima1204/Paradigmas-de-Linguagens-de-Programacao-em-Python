idade = int(input("Informe sua idade: "))
maior_idade = idade >= 18
if maior_idade:
    print("Voce é maior de idade")
else:
    print("Voce é menor de idade!")
#Short-hand do if else    
print("Voce é maior de idade") if maior_idade else print("Voce é maior de idade")