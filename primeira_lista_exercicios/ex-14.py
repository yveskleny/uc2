texto = input("Copie e cole um texto qualquer: ")

qtd_de_letras = {letra: 0 for letra in "abcdefghijklmnopqrstuvwxyz"}
for letra in texto:
    if letra.lower() not in qtd_de_letras.keys():
        continue
    else:
        qtd_de_letras[letra] += 1

print(qtd_de_letras)