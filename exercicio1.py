def exec1():
    nota = input('Informe uma nota: ')
    nota = float(nota)
    while not nota <= 10 and nota >= 0:
        print('Informe uma nota entre 0 e 10!')
        return exec1()

exec1()
