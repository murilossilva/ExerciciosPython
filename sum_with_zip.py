from itertools import zip_longest

lista_a = [5, 10, 15, 20, 24, 70]
lista_b = [9, -1, 23, 5, 2.4,]
lista_soma = [valor_a + valor_b for valor_a, valor_b in zip_longest(lista_a, lista_b, fillvalue=0)]

print(lista_soma)
