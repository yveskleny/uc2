# 214 / 2 = 107 resto 0
# 107 / 2 = 53 resto 1
# 57 / 2 = 26 resto 1
# 26 / 2 = 13 resto 0
# 13 / 2 = 6 resto 1
# 6 / 2 = 3 resto 0
# 3 / 2 = 1 resto 1

# 11010110
# 128 + 64 + 0 + 16 + 0 + 4 + 2 + 0

def converte_d2b(numero_decimal):
    numero_binario = ""

    while(numero_decimal > 1):
        resto = numero_decimal % 2
        numero_decimal //= 2
        numero_binario += str(resto)

    numero_binario += str(numero_decimal)

    return numero_binario[::-1]

for i in range(256):
    print(i, converte_d2b(i))