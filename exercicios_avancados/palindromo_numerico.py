def palindromo_numerico(numero):
    numero_str = str(numero)
    if numero_str == numero_str[::-1]:
        return True
    return False

print(palindromo_numerico(555))
print(palindromo_numerico(5551))
print(palindromo_numerico(11555))
print(palindromo_numerico(5515))
print(palindromo_numerico(51515))
print(palindromo_numerico(5055))
print(palindromo_numerico(150050051))