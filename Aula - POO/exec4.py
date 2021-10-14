class Pessoa:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def envelhecer(self):
        self.age = self.age + 1
        _str = (f'Agora {self.name} tem {self.age} anos de idade')
        if self.age < 21:
            self.height += 0.05
            print(f'{self.name} cresceu e agora tem {self.height} cm'
                  ' de altura!')
        return _str
        
    def engordar(self, weight):
        self.weight = self.weight + weight
        _str = (f'{self.name} acabou comendo demais e engordou {weight}kg,'
                f' agora o seu peso é de {self.weight}kg.')
        return _str

    def emagrecer(self, weight):
        self.weight = self.weight - weight
        _str = (f'{self.name} está pegando pesado na academia,'
                f' por conta disso acabou emagrecendo {weight}kg!'
                f' Seu peso atual é de {self.weight}kg.')
        return _str
        

    def crescer(self, height):
        self.height = self.height + height
        _str = (f'Uau, alguém comeu fermento! {self.name} acabou de crescer'
                f' {height} cm. Sua altura passou a ser de {self.height}.')
        return _str

Murilo = Pessoa(name = 'Murilo', age = 23, weight = 75, height = 1.78)
print(f'\nNome: {Murilo.name}\nIdade: {Murilo.age} anos'
      f'\nPeso:{Murilo.weight}kg\nAltura:{Murilo.height}m\n')
