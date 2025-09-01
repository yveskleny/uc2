produtos = [('Caneta', 2.50), ('Caderno', 15.00), ('Borracha', 1.75), ('Mochila', 50.00)]


produtos_ordenados = sorted(produtos, key= lambda produto: -produto[1])

print(produtos_ordenados)
