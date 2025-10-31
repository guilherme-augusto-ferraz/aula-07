def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor não pode ser zero.")
    return a / b

try:
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print("Erro capturado:", e)

