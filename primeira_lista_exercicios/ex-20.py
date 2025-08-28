class Produto:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto

    def calcula_desconto(self):
        return self.preco * (1 - (self.desconto) / 100)

# Produto(Nome, Valor, Desconto(%))
prod_teste = Produto("Geladeira", 6000, 50)
print(prod_teste.calcula_desconto())

