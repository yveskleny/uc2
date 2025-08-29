numero_recebido = int(input("Digite um número: "))

count = 0
divisores = []
for i in range(1, numero_recebido+1):
    if numero_recebido % i == 0:
        count += 1
        divisores.append(i)

print("divisores:", divisores)

if count == 2:
    print(f"{numero_recebido} é primo!")
else:
    print(f"{numero_recebido} não é primo.")