lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comuns = []

# for elemento in lista1:
#     if elemento in lista2:
#         comuns.append(elemento)

comuns = set(lista1) & set(lista2)

print(comuns)