def expo_manual(base, expoente):

    resultado = 1

    if expoente == 0:
        return 1

    for _ in range(abs(expoente)):
        resultado *= base

    if expoente < 0:
        return 1/resultado
    else:
        return resultado
    


for b in range(1, 10):
    for e in range(-5, 5):
        print(f"{b}^{e} = {expo_manual(b, e):.5f}")
    print()