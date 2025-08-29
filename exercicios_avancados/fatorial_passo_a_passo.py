def fatorial_passo_a_passo(numero):
    numeros = []

    resultado = 1
    for i in range(numero, 0, -1):
        resultado *= i
        numeros.append(i)

    
    resp = f"{numero}! = {" x ".join(map(str, numeros))} = {resultado}"

    print(resp) 



for i in range(1, 10):
    fatorial_passo_a_passo(i)