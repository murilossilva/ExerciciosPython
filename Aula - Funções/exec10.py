import numpy.random as np

aux = 0
dados = np.randint(1,6,2)

def menu():
    main = input('\nGostaria de tentar novamente? [s/n] ')
    if main == 'n':
        return False
    if main == 's':
        return True

def soma_dados(dados):
    first = 0
    for i in dados:
        first += i
    return first

def de_novo():
    dados_2 = np.randint(1,6,2)
    sec = 0
    for k in dados_2:
        sec += k
    return sec

def resultado():
    if soma_dados(dados) ==  7 or soma_dados(dados) == 11:
        print('Você ganhou! xD'),
        return False
        
    if soma_dados(dados) == 3 or soma_dados(dados) == 2 or soma_dados(dados) == 12:
        print('C-R-A-P-S! Você perdeu! x.x'),
        return False

    else:
        print(f'Ponto! Tente tirar novamente um {soma_dados(dados)}.')
        return True

print('Você tirou', soma_dados(dados))

if resultado() == True:
    while menu() == True:
        aux = de_novo()
        if aux == (soma_dados(dados)):
            print(f'Você tirou novamente um {aux} e ganhou! xD')
            break
        elif aux == 7:
            print(f'Você tirou um {aux} e perdeu! x.x')
            break
        else:
            print(f'Você tirou um {aux}. Tente novamente!')
        
            
