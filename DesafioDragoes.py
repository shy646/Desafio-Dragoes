C = int(input("Digite o número de casos de teste: "))

for _ in range(C):
    N = int(input("Digite o nível de energia: "))

    if N > 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")
