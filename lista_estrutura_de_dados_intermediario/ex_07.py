lista_aninhada = [[1, 2], [3, 4, 5], [6]]

lista_plana = [elemento for lista in lista_aninhada for elemento in lista]

print(lista_plana)

