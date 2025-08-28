def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado

def fatorial_recursivo(numero):
    if numero == 1:
        return 1
    numero *= fatorial_recursivo(numero - 1)
    
    return numero

print(fatorial_recursivo(3))