def valorPagamento(valor,dias):
    if dias == 0:
        return valor
    else:
        valor = valor * (1.03 + (0.001 * dias))
        return valor

valor = -1
relatorio = 0
contas = 0

print('Olá, seja bem-vindo! Caso deseje sair é só digitar 0 no campo de valor, '
      'se houver algum dado já inserido, será mostrado um extrato do dia.\n')
while True:
    valor = input('Informe o valor da prestação: ')
    valor = float(valor)
    if valor != 0:
        dias = input('\nQuantos dias de atraso a prestação possui? ')
        dias = int(dias)
        valorPagamento(valor,dias)
        print('\nO valor da sua prestação é de R$', valorPagamento(valor, dias),
              '\n','='*50)
        relatorio += valorPagamento(valor,dias)
        contas += 1
    else:
        print('\nValores do dia: R$', relatorio,'\nNúmeros de contas pagas:',
              contas)
        
        break
