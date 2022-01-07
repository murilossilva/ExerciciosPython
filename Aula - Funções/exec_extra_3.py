def soma_percentual(n1, percentual):
    print(f'{n1 * (1 + (int(percentual)/100))}')

n1 = int(input('Insira um valor a ser somado: '))
percentual = input('Insira o valor percentual a ser somado ao número anterior [ex.: 20%] ')

percentual = percentual.split('%')

while not percentual[0].isnumeric():
    percentual = input('Por favor, insira o valor percentual a ser somado ao número anterior [ex.: 20%] ')
    percentual = percentual.split('%')
    
soma_percentual(n1, percentual[0])
