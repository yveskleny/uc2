soma = 0
while True:
    numero = int(input("Digite um numero: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        soma += numero  
print(soma)
