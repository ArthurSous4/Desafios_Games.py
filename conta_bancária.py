class ContaBancaria:
    def __init__(self,numeroDaConta,titularConta,saldo=float(0),chequeEspLmt=0,chequeEspSaldo=0):
        self.numeroDaConta = numeroDaConta
        self.titularConta = titularConta
        self.saldo = saldo
        self.chequeEspLmt = chequeEspLmt
        self.chequeEspSaldo = chequeEspSaldo

    def depositarValor(self,valor):
        if valor <= 0:
            print("Valor inválido para deposito, voltando ao menu inicial ")
        else:
            if self.chequeEspSaldo != 0:
                valor -= self.chequeEspSaldo

            self.saldo += valor
            print(f"O valor de {valor} R$ foi adicionado á carteira")

    def sacarValor(self,valor):
        if valor <=0 or valor > self.saldo:
            if 
        
        
                print("Valor inválido para saque, voltando ao menu inicial ")
                
                
        else:
            self.saldo -= valor
            print(f"O valor de {valor} R$ foi sacado da sua carteira")

    def transferirValor(self,valor,contadestino):
        if valor > self.saldo or valor == 0:
            print("voçe não tem saldo suficiente para realizar a tranferencia, voltando ao menu")
        else:
            self.saldo -= valor
            contadestino.depositarValor(valor)

    def consultarSaldo(self):
        print(f"O saldo da conta é: {self.saldo}")


#contas testes

maria=ContaBancaria("2811", "Maria Da Silva", 0, 100,20)
joao=ContaBancaria("0520", "Joao Albuquerque", 0, 150,0)

joao.depositarValor(100)
joao.sacarValor(50)
joao.transferirValor(50, maria)
maria.consultarSaldo()
joao.consultarSaldo()
maria.depositarValor(20)
maria.consultarSaldo()
