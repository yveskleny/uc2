class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        else:
            self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo Insuficiente")
        elif valor <= 0:
            print("Valor informado inválido.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
            return valor
        
    def ver_saldo(self):
        print(f"Seu saldo é de {self.saldo}")



conta_test = ContaBancaria()

conta_test.ver_saldo()
conta_test.sacar(1000)
conta_test.ver_saldo()
conta_test.depositar(1000)
conta_test.ver_saldo()
conta_test.sacar(5000)
conta_test.ver_saldo()
conta_test.sacar(-5000)
conta_test.ver_saldo()
conta_test.depositar(-5000)
conta_test.ver_saldo()
conta_test.sacar(500)
conta_test.ver_saldo()



