def retangulo(row, col):
    #tratamento das dimensões
    if row > 20:
        row = 20
    elif row < 1 or row == '':
        row = 1
    if col > 20:
        col = 20
    elif col < 1 or col == '':
        col = 1

    #cria a linha
    def create_row(row):
        linha = '+'
        for i in range(row):
            linha += '-'
        linha += '+'
        print(linha)

    #cria a coluna
    def create_col(row, col):
        for k in range(col):
            coluna = '|'
            coluna += ' ' * row
            coluna += '|'
            print(f'{coluna }')

    create_row(row), create_col(row,col),create_row(row)
    
row = input('Digite a largura do polígono: ')
row = int(row)
col = input('Digite a altura do polígono: ')
col = int(col)

retangulo(row, col)
