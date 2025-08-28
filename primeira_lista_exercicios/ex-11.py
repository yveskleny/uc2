lista_de_palavras = []

for i in range(10):
    lista_de_palavras.append(input("Digite a palavra de deseja inserir na lista: "))

palavra_buscada = input("Insira a palavra a ser buscada: ")

numero_de_ocorrencias = 0
for palavra in lista_de_palavras:
    if palavra_buscada == palavra:
        numero_de_ocorrencias += 1

print(f'A palavra "{palavra_buscada}" aparece {numero_de_ocorrencias} vezes na lista.')