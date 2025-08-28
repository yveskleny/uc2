idade = int(input("Qual a sua idade: "))

if idade >= 18:
    print("Adulto")
elif idade >= 14:
    print("Juvenil")
elif idade >= 9:
    print("Infantil")
elif idade < 9:
    print("Mirim")