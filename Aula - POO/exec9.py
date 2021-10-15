import numpy.random as np

class Macaco:
    def __init__(self, name, bucho):
        self.name = name
        self.bucho = bucho

    def comer(self, alimento):
        if alimento == 'banana':
            self.bucho += 10
            print(f'\n{self.name} comeu uma banana!')
        elif alimento == 'maçã':
            self.bucho += 5
            print(f'\n{self.name} comeu uma maçã!')
        elif alimento == 'amendoim':
            self.bucho += 2
            print(f'\n{self.name} comeu um pouco de amendoim!')
        elif alimento == 'outro macaco':
            for i in range(len(list(macacos))):
                print(i, macacos[i].name)

            del_monkey = int(input('\nVocê gostaria de devorar qual macaco?\nResposta (Informe o índice): '))
            while macacos[del_monkey].name == self.name:
                del_monkey = int(input('\nVocê não pode se comer!\nDigite uma opção que seja válida: '))
            _str = print(f'\nO macaco {macacos[del_monkey].name} foi devorado pelo macaco {self.name}! :O')
            del_monkey = macacos.pop(del_monkey)
            print(f'\nOs macacos que sobraram foram: ')
            for i in range(len(list(macacos))):
                print (i, macacos[i].name)
            

        if self.bucho > 100:
            self.bucho = 100
            print(f'\nO bucho dele já está cheio e não aguenta mais comer {alimento}!')

    def verBucho(self):
        _str = print(f'\nO macaco {self.name} está com {self.bucho}%'
                     ' do bucho cheio.')
        return _str

    def digerir(self):
        if self.bucho >= 5:
            self.bucho -= 5
        else:
            self.bucho = 0
        _str = print(f'\nO macaco {self.name} digeriu e o seu bucho agora está'
                     f' {self.bucho}% cheio')
        return _str

#inicia o programa
NumMacacos = int(input('Quantos macacos serão alimentados? '))

macacos = list()
for i in range(NumMacacos):
    name = input('Qual o nome do macaco? ').capitalize()
    bucho = np.randint(0, 100, 1)
    macacos.append(Macaco(name, bucho))
    print(f'O macaco {name} foi criado e o seu bucho está {bucho}% cheio\n')

while True:
    print("""\n--------------------------------------------------\n""")
    escolheMacaco = int(input('\nQual macaco você quer executar alguma ação? \n(O primeiro macaco está na posição 0).\n\nResposta: '))
    resp = int(input(f'\nO que você gostaria de fazer com o {macacos[escolheMacaco].name}? \n'
                 f'\n1 - Comer\n2 - Ver o bucho dele\n3 - Digerir\n\nResposta: '))
    if resp == 1:
        alimento = (input(f'Escolha o alimento que você gostaria de dar para o {macacos[escolheMacaco].name}\n'
                      '\nbanana\nmaçã\namendoim\noutro macaco\n\nResposta: '))
        macacos[escolheMacaco].comer(alimento)

    if resp == 2:
        macacos[escolheMacaco].verBucho()

    if resp == 3:
        macacos[escolheMacaco].digerir()
