class ContaBancaria:
    def __init__(self,numeroDaConta,titularConta,saldo=float(0)):
        self.numeroDaConta = numeroDaConta
        self.titularConta = titularConta
        self.saldo = saldo

    def depositarValor(self):
        self.valor = float(input("digite o valor que deseja depositar: "))
        if self.valor <= 0:
            print("Valor inválido para deposito, voltando ao menu inicial ")
        else:
            self.saldo += self.valor
            print(f"O valor de {self.valor} R$ foi adicionado á sua carteira")

    def sacarValor(self):
        self.valor = float(input("digite o valor que deseja sacar: "))
        if self.valor <=0 or self.valor > self.saldo:
            print("Valor inválido para saque, voltando ao menu inicial ")
        else:
            self.saldo =- self.valor
            print(f"O valor de {self.valor} R$ foi sacado da sua carteira")




#

maria=ContaBancaria("2811", "maria malamada", 0)
joao=ContaBancaria("0520", "joao albuq", 0)

joao.depositarValor()
print(f"Seu extrato é: {joao.saldo} R$")
joao.sacarValor()
print(f"Seu extrato é: {joao.saldo} R$")





