class ContaCorrente:
    def __init__(self, num_conta, name, saldo = 0):
        self.num_conta = num_conta
        self.name = name
        self.saldo = saldo

    def _set_name(self, name):
        self.name = name
        _str = (f'O nome do correntista foi alterado para {self.name}')
        return _str

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        _str = (f'O saldo atual é de R${self.saldo}.')
        return _str

    def sacar(self, saque):
        if self.saldo < saque:
            print(f'O valor de R${saque} não pode ser sacado pois há'
                  f' R${self.saldo} em sua conta.')
        else:
            self.saldo = self.saldo - saque
            _str = (f'Saque realizado com sucesso!'
                    f'Saldo atual da conta: R${self.saldo}')
            return _str
