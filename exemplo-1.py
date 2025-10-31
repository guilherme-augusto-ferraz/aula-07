try:
    numero = int(input("Digite um número inteiro: "))
    print(10 / numero)
except Exception as e:
    print("Ocorreu um erro: ", e)