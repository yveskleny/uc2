lista_de_produtos = []

for _ in range(5):
    produto = input("Digite o nome dos item que deseja adicionar no carrinho: ")
    lista_de_produtos.append(produto)

for item in sorted(lista_de_produtos):
    print(item)