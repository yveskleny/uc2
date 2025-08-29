def verificar_armstrong(numero):
    num_str = str(numero)

    pot = len(num_str)

    soma = 0
    for letra in num_str:
        soma += int(letra)**pot
    
    if soma == numero:
        return True
    
    return False

    
numeros_teste = [1, 153, 154, 370, 371, 372, 407, 1634, 4444, 8208, 9474]

for num in numeros_teste:
    print(num, verificar_armstrong(num))