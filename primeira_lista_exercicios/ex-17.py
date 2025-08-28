def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = int(input("Escolha uma das operações que deseja realizar: "))

if op == 1:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print(f"{n1} + {n2} = {somar(n1, n2)}")

elif op == 2:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print(f"{n1} - {n2} = {subtrair(n1, n2)}")

elif op == 3:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print(f"{n1} * {n2} = {multiplicar(n1, n2)}")

elif op == 4:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print(f"{n1} / {n2} = {dividir(n1, n2):.4f}")
