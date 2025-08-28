lista_de_usuarios = []

for i in range(1, 4):
    usuario = dict()
    usuario["nome"] = input(f"Digite o nome do usuario {i}: ")
    usuario["idade"] = int(input(f"Digite a idade do usuario {i}: "))
    usuario["email"] = input(f"Digite o email do usuario {i}: ")
    lista_de_usuarios.append(usuario)

for user in lista_de_usuarios:
    print(user)