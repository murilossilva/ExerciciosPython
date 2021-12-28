from random import randint
cpfs_gerados = 0

cont = input('Quantos CPFs você quer gerar? ')

while cpfs_gerados < int(cont):
    primeiros_numeros = str(randint(100000000, 999999999))
    i = 0
    lista_numeros = []
    cpf = ''

    # multiplica os 9 primeiros dígitos pelos índices e os insere numa lista
    for num in range(10, 1, -1):
        mult_primeiros_numeros = int(primeiros_numeros[i]) * num
        lista_numeros.append(mult_primeiros_numeros)
        i += 1

    soma_primeiro_dig = sum(lista_numeros)

    # fórmula para descobrir qual será o próximo dígito
    primeiro_dig = 11 - (soma_primeiro_dig % 11)

    primeiro_dig = 0 if primeiro_dig > 9 else primeiro_dig

    j = 0
    lista_numeros_2 = []
    segundo_numero = primeiros_numeros + str(primeiro_dig)

    # multiplica os 9 primeiros digitos + o digito final 1 pelos
    # indices e os insere numa lista_2
    for num in range(11,1,-1):
        mult_segundo_digito = int(segundo_numero[j]) * num
        lista_numeros_2.append(mult_segundo_digito)
        j += 1

    # fórmula para descobrir o próximo dígito
    soma_segundo_dig = sum(lista_numeros_2)

    segundo_dig = 11 - (soma_segundo_dig % 11)
    segundo_dig = 0 if segundo_dig > 9 else segundo_dig

    digitos_finais = str(primeiro_dig) + str(segundo_dig)

    print(f'{primeiros_numeros[:3]}.{primeiros_numeros[3:6]}.{primeiros_numeros[6:9]}'
          f'-{digitos_finais}')
    cpfs_gerados += 1
