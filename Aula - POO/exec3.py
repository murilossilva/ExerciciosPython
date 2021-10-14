class retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def _set_lados(self, base, altura):
        self.base = base
        self.altura = altura
        _str = (f'Agora o retângulo tem base no valor de {self.base} cm e'
               f' altura de {self.altura} cm.')
        return _str

    def _get_lados(self):
        _str = (f'O retângulo tem base no valor de {self.base} cm e'
               f' altura de {self.altura} cm.')
        return _str

    def Calc_area(self):
        area = self.base * self.altura
        _str = (f'Serão necessários {area} cm² de piso para preencher a área.')
        return _str

    def Calc_perimeter(self):
        perimeter = (self.base * 2) + (self.altura * 2)
        _str = (f'Já para preencher o perímetro será necessário {perimeter} cm'
                ' de rodapé.')
        return _str

def main():
    base = input('Digite o valor da base da área: ')
    base = float(base)
    altura = input('Digite o valor da altura da área: ')
    altura = float(altura)
    retangulo_main = retangulo(base = base, altura = altura)
    print(retangulo_main.Calc_area())
    print(retangulo_main.Calc_perimeter())


if __name__ == '__main__':
    main()
