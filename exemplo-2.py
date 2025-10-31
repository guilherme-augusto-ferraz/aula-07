try:
    num = int(input("Digite um número: "))
    resultado = 10 / num
except ZeroDivisionError:
    print("Divisão por zero!")
else:
    print(f"Resultado: {resultado}")

