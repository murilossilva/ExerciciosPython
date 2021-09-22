def exec2():
    nome = input('Insira o seu nome: ')
    nome = str(nome)
    pwd = input('Insira uma senha: ')

    while pwd == nome:
        print('A senha deve ser diferente do seu nome!')
        return exec2()

exec2()
