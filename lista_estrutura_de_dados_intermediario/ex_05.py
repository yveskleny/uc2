notas = {'Ana': 8.5, 'Beto': 9.2, 'Carla': 7.8, 'Daniel': 9.5}

nome_melhor_aluno = ""
maior_nota_encontrada = 0


for nome, nota in notas.items():
    if nota > maior_nota_encontrada:
        maior_nota_encontrada = nota
        nome_melhor_aluno = nome
    

print(f"O aluno com a maior nota é {nome_melhor_aluno} com {maior_nota_encontrada}.")