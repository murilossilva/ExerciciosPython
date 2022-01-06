def saudacao(msg, nome):
    print(f'{msg}, {nome}! Seja bem-vindo ao nosso programa!')

msg = ''
nome = ''

while not msg.isalpha() or not nome.isalpha():
    print('Olá! Insira apenas letras para continuar o programa!')
    msg = input('Insira uma saudação: ')
    nome = input('Informe o seu nome: ')
        
saudacao(msg, nome)
