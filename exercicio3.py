def name():
    nome = input('Insira o seu nome: ')
    nome = str(nome)
    a = len(nome)
    while a < 3:
        name()

def age():
    idade = input('Insira a sua idade: ')
    idade = int(idade)
    while idade < 0 or idade > 150:
        return age()

def salario():
    sal = input('Insira o seu salário: ')
    sal = float(sal)
    if not sal > 0:
        return salario()
    

def sex():
    sexo= input('Qual o seu sexo?[F/M] ')
    sexo = str(sexo)
    while not (sexo == 'F' or sexo == 'M'):
        return sex()

def estado_civil():
    civil = input('Qual o seu estado civil?\ns - solteiro(a)\nc - casado(a)\nv - viúvo(a)\nd - divorciado(a)\n')
    civil = str(civil)
    while not (civil == 'c' or civil == 'v' or civil == 'd' or civil == 's'):
        return estado_civil()


def exec3():
    name(), print('')
    age(), print('')
    salario(), print('')
    sex(), print('')
    estado_civil()

exec3()
