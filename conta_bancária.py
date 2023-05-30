class ContaBancaria:
    def __init__(self,numeroDaConta,titularConta,saldo=float(0),chequeEspLmt=0,chequeEspSaldo=0):
        self.numeroDaConta = numeroDaConta
        self.titularConta = titularConta
        self.saldo = saldo
        self.chequeEspLmt = chequeEspLmt
        self.chequeEspSaldo = chequeEspSaldo

    def depositarValor(self,valor):
        if valor <= 0:
            print("Valor inválido para depósito, voltando ao menu inicial")
        else:
            if self.chequeEspSaldo != 0:
                if valor >= self.chequeEspSaldo:
                    valor -= self.chequeEspSaldo
                    self.chequeEspSaldo = 0
                else:
                    self.chequeEspSaldo -= valor
                    valor = 0
            else:
                self.saldo += valor
                print(f"O valor de {valor} R$ foi adicionado à carteira")

    def sacarValor(self,valor):
        if valor > self.saldo:
            if valor > self.saldo + self.chequeEspLmt:
                print("Valor inválido para saque, limite do cheque especial foi excedido")
            else:
                self.chequeEspSaldo = valor - self.saldo
                self.saldo = 0
                print(
                    f"O usuário {self.titularConta} sacou {valor} R$, e está devendo {self.chequeEspSaldo} R$ ao cheque especial")
        elif valor <= 0:
            print("Valor inválido para saque, voltando ao menu inicial")
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

    def consultarChequeEsp(self):
        print(f"O saldo do seu cheque especial é {self.chequeEspSaldo}R$ e seu limite é de {self.chequeEspLmt}R$")


#contas testes

maria=ContaBancaria("2811", "Maria Da Silva", 0, 100,20)
joao=ContaBancaria("0520", "Joao Albuquerque", 0, 150,0)

joao.depositarValor(100)
joao.sacarValor(250)
joao.depositarValor(20)
joao.consultarChequeEsp()
joao.depositarValor(20)