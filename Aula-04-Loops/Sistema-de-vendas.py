#========================== MINHA SOLUCAO ===================================
# lista_produtos = []
# opcao = int(input("Digite 1 para Comprar e 2 para sair: "))
# while True:
#     if opcao == 1:
#         nome_produto = input("Digite o nome do produto: ")
#         preco_unitario = float(input("Digite o preco do produto: "))
#         quant_comprada = int(input("Digite a quantidade total comprada: "))
#         valor_total_produto = preco_unitario * quant_comprada
#         produto = dict({"Nome Produto": nome_produto, "Preco Unitario": preco_unitario, "Quantidade": quant_comprada,
#         "Valor total produto": valor_total_produto
#         })
#         lista_produtos.append(produto)
#         opcao = int(input("Digite 1 para Comprar e 2 para sair: "))
#         continue
#     else:
#         print("Saindo ....")
#         break
#
# for x in lista_produtos:
#     print(f"O Valor total do produto {x["Nome Produto"]}: {x["Valor total produto"]}")


# ======================= SOLUCAO PROFESSOR ==============================
qtd_itens = int(input("Informe quantos itens: "))
total_geral_compra: float = 0.0
produto_mais_caro: str = ""
lista_valores: list = []
lista_produtos: list = []

for cont in range(1, qtd_itens + 1):
    qtd_total_produto = 0
    total_produto = 0.0
    print(f"\nProduto {cont}: ")
    nome = input("Digite o nome do produto: ")
    valor = float(input("Informe o valor do produto: "))
    qtd_total_produto = int(input("Informe quantos itens de produtos: "))
    total_produto = valor * qtd_total_produto
    produto = (nome, valor, qtd_total_produto, total_produto)
    lista_produtos.append(tuple(produto))
    lista_valores.append(valor)
    total_geral_compra += total_produto
    produto_mais_caro = max(lista_valores)
    for produto in lista_produtos:
        print(f"Nome: {produto[0]}")
        print(f"Valor: {produto[1]}")
        print(f"Qtd total: {produto[2]}")
        print(f"Valor total: {produto[3]}")
print(produto_mais_caro)


