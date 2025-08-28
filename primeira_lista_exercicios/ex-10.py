lista_numeros = []

for i in range(10):
    lista_numeros.append(int(input(f"Digite o {i+1} numero: ")))

print(f"O maior número é : {max(lista_numeros)}")
print(f"O menor número é : {min(lista_numeros)}")

media = sum(lista_numeros)/len(lista_numeros)

print(f"A média dos valores é : {media}")

