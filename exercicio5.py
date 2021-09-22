def exec5():
    a = 80000
    tax_a = 1.03
    b = 200000
    tax_b = 1.015
    anos = 0

    while b > a:
        a = a * tax_a
        b = b * tax_b
        anos += 1

    print('A população de A irá se igualar com a de B em {} anos'.format(anos))
    
exec5()
