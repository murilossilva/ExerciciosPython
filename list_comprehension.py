string = '01234567890123456789012345678901234567890123456789'
lista_de_strings = [string[:10] for strings in range(4)]

retorno_strings = '.'.join(lista_de_strings)
print(retorno_strings)
