estoque_atual = {'Caneta': 100, 'Caderno': 50, 'Lápis': 75}
nova_remessa = {'Caderno': 25, 'Borracha': 30, 'Caneta': 50}

for produto, remessa in nova_remessa.items():
    if produto not in estoque_atual.keys():
        estoque_atual.update({produto: remessa})
    else:
        estoque_atual[produto] += remessa

print(estoque_atual)