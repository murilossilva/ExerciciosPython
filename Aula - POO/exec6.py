'''
Classe TV: Faça um programa que simule um televisor
criando-o como um objeto. O usuário deve ser capaz de informar o
número do canal e aumentar ou diminuir o volume. Certifique-se de que o
número do canal e o nível do volume permanecem dentro de faixas válidas.

'''

class TV:
    def __init__(self, NumCanal, volume = 20):
        while NumCanal > 99 or NumCanal < 1 or type(NumCanal) == type(int):
            NumCanal = input('Insira um número de canal inteiro e que seja válido: ')
            NumCanal = int(NumCanal)
        while volume < 0 or volume > 100 or type(volume) == type(int):
            volume = input('Insira um valor de volume inteiro entre 0 e 100: ')
            volume = int(volume)
        self.NumCanal = NumCanal
        self.volume = volume
        _str = print(f'Você está no canal {self.NumCanal},'
                f' o volume da sua TV está em {self.volume}.')

    def _set_canal(self, NumCanal):
        while NumCanal > 99 or NumCanal < 1 or type(NumCanal) == type(int):
            NumCanal = input('Insira um número de canal inteiro e que seja válido: ')
            NumCanal = int(NumCanal)        
        self.NumCanal = NumCanal
        _str = (f'Você mudou a sua TV para o canal {self.NumCanal}')
        return _str

    def aumentar_vol(self):
        if self.volume < 100:
            self.volume += 1
            _str = (f'Você aumentou o volume da sua TV. Ele agora está em {self.volume}')
            return _str
        
        else:
            _str = (f'Sua TV já está no volume máximo!')
            return _str

    def diminuir_vol(self):
        if self.volume > 0:
            self.volume -= 1
            _str = (f'Você diminuiu o volume da sua TV. Ela agora está em {self.volume}')
            return _str
        else:
            _str = (f'Sua TV já está no mudo. Não é possível diminuir o volume.')
            return _str
