def divisao(a , b):
    try:
        return a / b
    except TypeError:
        print(f'Os valores devem ser do tipo int ou float.')
    except ZeroDivisionError:
        print(f'O divisor deve ser diferente de zero!')
