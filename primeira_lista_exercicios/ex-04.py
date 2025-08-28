primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
operacao = input("Entre com um das operações (+ - * /): ")

if operacao == "+":
    print(primeiro_numero + segundo_numero)
elif operacao == "-":
    print(primeiro_numero - segundo_numero)
elif operacao == "*":
    print(primeiro_numero * segundo_numero)
elif operacao == "/":
    print(primeiro_numero / segundo_numero)
    
