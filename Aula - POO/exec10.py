class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        valor = float(input('Insira o valor que quer abastecer: '))
        abastecer = valor/self.valorLitro
        if abastecer <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= abastecer
        _str = print(f'Quantia de combustível restante na bomba: '
                     f'{self.quantidadeCombustivel} litros.')
        return _str

    def abastecerPorLitro(self):
        litro = float(input('Insira a quantidade de litros a serem abastecidos: '))
        if litro <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litro
        _str = print(f'Quantia de combustível restante na bomba: '
                     f'{self.quantidadeCombustivel} litros.')
        return _str

    def alterarValor(self):
        valor = float(input('Insira o novo valor do combustível: '))
        self.valorLitro = valor
        _str = print(f'O novo preço do combustível é de RS{self.valorLitro}')
        return _str

    def alterarCombustivel(self):
        outroCombustivel = input('Insira o novo nome do novo combustível: ')
        self.tipoCombustivel = outroCombustivel

    def alterarQuantidadeCombustivel(self):
        quantidadeCombustivel = float(input('Insira a quantidade de combustivel'
                                            ' presente na bomba: '))
        self.quantidadeCombustivel = quantidadeCombustivel
        _str = print(f'A bomba agora possui {self.quantidadeCombustivel}'
                     f' litros de {self.tipoCombustivel}.')
