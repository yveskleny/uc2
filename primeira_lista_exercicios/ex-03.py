nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("ALUNO APROVADO")
elif media >= 5 and media < 7:
    print("ALUNO EM RECUPERAÇÃO")
elif media < 5: 
    print("ALUNO REPROVADO")