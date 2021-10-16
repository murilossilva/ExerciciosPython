def divisao(a , b):
    try:
        print(a / b)
    except TypeError:
        print(f'Os valores devem ser do tipo int ou float.')
    except ZeroDivisionError:
        print(f'O divisor deve ser diferente de zero!')

def main():
    try:
        a = float(input('Insira um valor para o dividendo: '))
        b = float(input('Insira um valor para o divisor: '))
        divisao(a, b)
    except ValueError:
        print(f'Os valores devem ser do tipo int ou float.')

if __name__ == '__main__':
    main()
