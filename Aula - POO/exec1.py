class Bola:
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def _set_cor(self, cor):
        '''
        Altera a cor de um objeto da classe Bola.

        Comando:
        nome_do_objeto._set_cor('cor-que-vai-alterar')
        '''
        self.cor = cor
        print(f'Cor alterada para {self.cor}.')


    def _get_cor(self):
        '''
        Printa no terminal a cor atual de um objeto da classe Bola.

        Comando:
        nome_do_objeto._get_cor()

        '''
        return self.cor

        
