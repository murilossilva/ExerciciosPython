def soma(n1, n2, n3):
    print(float(n1) + float(n2) + float(n3))

while True:
    print('Olá! Insira apenas números para continuar o programa!')
    n1 = input('Insira o primeiro número a ser somado: ')
    n2 = input('Insira o segundo número a ser somado: ')
    n3 = input('Insira o terceiro e último número a ser somado: ')

    if (n1.isnumeric() and n2.isnumeric() and n3.isnumeric()):
        break
    else:
        continue
    
soma(n1, n2, n3)
