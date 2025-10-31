class SaldoInsuficiente(Exception):
    """Exceção lançada quando o saldo é insuficiente."""
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(f"Saldo insuficiente: saldo {saldo}, tentativa de saque {valor}")


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficiente(self.saldo, valor)
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

# Programa principal
conta = ContaBancaria("João", 1000)
try:
    conta.sacar(1500)
except SaldoInsuficiente as e:
    print(e)

