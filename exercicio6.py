def exec5():
    a = input('Insira a população de A: ')
    a = int(a)
    tax_a = input('Insira a taxa populacional de A: ')
    tax_a = float(tax_a)
    b = input('Insira a população de B: ')
    b = int(b)
    tax_b = input('Insira a taxa populacional de B: ')
    tax_b = float(tax_b)
    anos = 0

    if b > a:
        while b > a:
            a = a * tax_a
            b = b * tax_b
            anos += 1
        print('A população de A irá se igualar ou ultrapassar a de B em {} anos'.format(anos))
    else:
        while b < a:
            a = a * tax_a
            b = b * tax_b
            anos += 1
        print('A população de B irá se igualar ou ultrapassar a de A em {} anos'.format(anos))

exec5()
