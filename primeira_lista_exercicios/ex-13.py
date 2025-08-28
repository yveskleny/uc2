boletim_alunos = []

for i in range(1, 6):
    aluno = dict()
    aluno["nome"] = input(f"Digite o nome do aluno {i}: ")
    aluno["nota 1"] = int(input(f"Digite a nota 1 do aluno {aluno["nome"]}: "))
    aluno["nota 2"] = int(input(f"Digite a nota 2 do aluno {aluno["nome"]}: "))
    aluno["nota 3"] = int(input(f"Digite a nota 3 do aluno {aluno["nome"]}: "))
    
    boletim_alunos.append(aluno)

for aluno in boletim_alunos:
    media = (aluno["nota 1"] + aluno["nota 2"] + aluno["nota 3"]) / 3
    print(f"A média do aluno {aluno["nome"]} é {media}")

