def verifica_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    return False


print(verifica_palindromo("osso"))
print(verifica_palindromo("arara"))
print(verifica_palindromo("radar"))
print(verifica_palindromo("texto"))

