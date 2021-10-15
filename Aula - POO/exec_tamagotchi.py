class Tamagotchi:
    def __init__(self, name, age, hungry = 40, health = 100, humor = 30):
        self.name = name.capitalize()
        while hungry < 1 or hungry > 100:
            hungry = input('Insira um valor válido (entre 1 e 100) para o campo de fome: ')
            hungry = int(hungry)
        self.hungry = hungry
        while health < 1 or health > 100:
            health = input('Insira um valor válido (entre 1 e 100) para o campo de saude.')
            health = int(health)
        self.health = health
        while age < 0 or type(age) != int:
            age = input('Insira uma idade que seja positiva e inteira: ')
            age = int(age)
        self.age = age
        self.humor = humor
        
#Setters
    def _set_name(self):
        name = input('Digite o novo nome do seu Tamagotchi: ')
        self.name = name
        _str = (f'O nome do seu Tamagotchi mudou para {self.name}.')
        return _str

    def _set_hungry(self, amount):
        if self.hungry < 10:
            self.hungry = 0
            bichinho._set_age()
        else:
            self.hungry -= 10 * amount
            if self.hungry < 0:
                self.hungry = 0
            bichinho._set_age()

    def _set_health(self):
        if self.health >= 90:
            self.health = 100
            bichinho._set_age()
        else:
            self.health += 10
            bichinho._set_age()
        self.hungry += 10
    def _set_age(self):
        self.age += 1
        print(f'O seu tamagotchi ficou mais velho, agora ele está com {self.age} anos de idade')

    def _set_die(self):
        self.health = 0
        self.hungry = 100
        print(f'Você matou o seu tamagotchi, você irá carregar essa culpa pra sempre!')

    def _set_humor(self, amount):
        if self.humor >= 90:
            self.humor = 100
            self.hungry = self.humor * amount
        else:
            self.humor += 10 * amount
            if self.humor > 100:
                self.humor = 100
            self.hungry += 3 * amount
            if self.hungry > 100:
                self.hungry = 100
        print(f'Você brincou com o seu tamagotchi por {amount} horas, agora o humor dele está em {self.humor} e a sua fome em {self.hungry}!')

    def _str_(self):
        print('\n-------------------- TOP SECRET --------------\n')
        _str = print(f'\nNome: {self.name}\nIdade: {self.age}\nSaúde: {self.health}\nFome: {self.hungry}\nHumor: {self.humor}')
        print('\n----------------------------------------------\n')
        return _str
        
#Getters
    def _get_name(self):
        print(f'O nome do seu tamagotchi é {self.name}.')

    def _get_hungry(self):
        print(f'O nível de fome do seu tamagotchi está em {self.hungry}.'
                f' Quanto maior ele estiver, mais fome ele está sentindo.')

    def _get_health(self):
        print(f'O nível de saúde do seu tamagotchi está em {self.health}.'
                f' Quanto menor ele estiver, menos saudável ele está.')

    def _get_age(self):
        print(f'A idade de {self.name} é {self.age}.')

    def _get_humor(self):
        humor = (self.health + self.humor) - self.hungry
        if humor < 0:
            humor = 0
        elif humor > 100:
            humor = 100
        print(f'O humor do seu tamagotchi está em {humor}.')

#Inicia o programa
nome = input('Qual será o nome do seu Tamagotchi? ')
idade = input('Qual será a idade do seu Tamagotchi? ')
idade = int(idade)
while idade < 0 or type(idade) != int:
    idade = input('Digite uma idade que seja positiva e inteira: ')

bichinho = Tamagotchi(name = nome, age = idade)
print(f'\nOlá, meu nome é {bichinho.name}!'
      """\n------------------------------------------\n
            ^__^
            (oo)\_______
            (__)\       )\/
                ||----w | 
                ||     ||\n""")
while (bichinho.health > 0) and (bichinho.hungry < 100):
    resp = input(f'O que você deseja fazer comigo agora?\n'
                f'\n1- Alimentar (-10 de fome por refeição)\n2- Dormir (+10 de saúde)\n3- Brincar (+10 de humor a cada hora e +3 de fome)\n4- Alterar nome'
                f'\n5- Visualizar humor\n6- Visualizar idade'
                f'\n7- Visualizar fome\n8- Visualizar saúde\n9- Visualizar nome\n10 - Matar o Tamagotchi\nResposta: ')
    print('\n')
    resp = int(resp)
    if resp == 1:
        amount = input('Quantas refeições você quer dar ao seu tamagotchi? ')
        amount = int(amount)
        bichinho._set_hungry(amount)
        print(f'O nível de fome do seu Tamagotchi agora é {bichinho.hungry}')
    elif resp == 2:
        bichinho._set_health()
        print(f'O seu tamagotchi dormiu bastante isso fez com que seu nível de saude aumentasse, o seu nível agora está em {bichinho.health}.')
    elif resp == 3:
        amount = input(f'Por quantas horas você pretende brincar com {bichinho.name}? ')
        amount = int(amount)
        bichinho._set_humor(amount)
    elif resp == 4:
        bichinho._set_name()
    elif resp == 5:
        bichinho._get_humor()
    elif resp == 6:
        bichinho._get_age()
    elif resp == 7:
        bichinho._get_hungry()
    elif resp == 8:
        bichinho._get_health()
    elif resp == 9:
        bichinho._get_name()
    elif resp == 10:
        bichinho._set_die()
    elif resp == 99:
        bichinho._str_()
    else:
        print('Escolha uma opção que seja válida: ')

print("""\n------------------------------------------\n
            ^__^
            (xx)\_______
            (__)\       )\\n
                ||----w |
                ||     ||\n\n\tVocê me deixou morrer!\n""")
