def opcoes():
    try:
        opcao = int(input('O que deseja fazer com a sua lista de tarefas?\n'
                          '1 - Adicionar nova tarefa;\n'
                          '2 - Listar tarefas;\n'
                          '3 - Desfazer última tarefa;\n'
                          '4 - Refazer última tarefa.\n\n'
                          'Insira uma das opções acima: '))
        print('-' * 80)
        return opcao
    except ValueError:
        print('Insira um valor que seja numérico e inteiro!')
        print('-' * 80)

def adiciona_tarefa():
    nova_tarefa = input('Qual tarefa deseja adicionar à sua lista?\n'
                        'Insira a sua tarefa: ')
    if nova_tarefa.isdigit():
        print('\nÉ necessário que a sua tarefa seja uma palavra!')
    else:
        todo_list.append(nova_tarefa.capitalize())
        redo_list.append(nova_tarefa.capitalize())
    print('-' * 80)

def lista_tarefas():
    if len(todo_list) == 0:
        print('Você não tem nenhuma tarefa para ser listada.')
    else:
        print('Suas tarefas são essas:')
    for indice, tarefa in enumerate(todo_list):
        print(f'{indice + 1} - {tarefa}')
    print('-' * 80)

def desfazer():
    try:
        todo_list.pop()
        print('Desfazendo última tarefa...')
    except IndexError:
        print('Não é possível desfazer uma lista sem tarefa!')
    print('-' * 80)

def refazer():
    try:
        print(f'Reanotando tarefa "{redo_list[len(todo_list)]}"')
        todo_list.append(redo_list[len(todo_list)])
    except IndexError:
        print('Você não possui tarefas para desfazer!')
    print('-' * 80)
    
if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        num_opcao = opcoes()
        if num_opcao in range(1,5):
            if num_opcao == 1:
                adiciona_tarefa()
            elif num_opcao == 2:
                lista_tarefas()
            elif num_opcao == 3:
                desfazer()
            else:
                refazer()
        else:
            print('Por favor, insira uma opção que seja entre 1 e 4!')
            print('-' * 80)
