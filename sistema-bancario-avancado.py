class ContaBancaria:
    
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.limite_diario = 3
        self.limite_saque = 500.00

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.limite_diario > 0 and valor <= self.limite_saque and self.saldo >= valor:
            self.saldo -= valor
            self.saques.append(valor)
            self.limite_diario -= 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif self.saldo < valor:
            print("Saldo insuficiente para saque.")
        else:
            print("Limite diário de saques atingido ou valor de saque inválido.")

    def extrato(self):
        print("\nExtrato:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso:
conta = ContaBancaria()
conta.depositar(1000.00)
conta.sacar(300.00)
conta.sacar(700.00)
conta.extrato()
