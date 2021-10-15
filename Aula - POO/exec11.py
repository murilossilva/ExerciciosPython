class Carro:
    def __init__(self, consumo, quantidadeCombustivel = 0):
        self.consumo = consumo
        print(f'O carro realiza {self.consumo} Km/L de gasolina')
        self.quantidadeCombustivel = quantidadeCombustivel

    def obterGasolina(self):
        return (f'O nível atual do tanque é de {self.quantidadeCombustivel} litros.')
    
    def adicionarGasolina(self,gas):
        self.quantidadeCombustivel += gas
        return (f'Foi abastecido um total de {gas} litro(s) de gasolina')
        
    def andar(self, km):
        combustivelConsumido = km/self.consumo
        if combustivelConsumido > self.quantidadeCombustivel:
            print(f'O tanque do veículo não tem gasolina o bastante para '
                  'andar esse trajeto')
        else:
            self.quantidadeCombustivel -= combustivelConsumido

        return (f'Você andou {km}Km e consumiu {combustivelConsumido} litros, restaram {self.quantidadeCombustivel}'
                ' de gasolina em seu tanque.')
