'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

'''

class Square:
    def __init__(self, lado):
        self.lado = lado

    def _set_lado(self, lado):
        self.lado = lado
        lado = lado * 4
        _str = (f'Agora o quadrado tem cada um de seus lados medindo {self.lado}cm'
              f' e uma área de {lado} cm²')

        return _str
        
    def _get_lado(self):
        lado = self.lado * 4
        _str = (f'O quadrado tem cada um de seus lados medindo {self.lado} cm'
              f' e uma área de {lado} cm²')

        return _str
