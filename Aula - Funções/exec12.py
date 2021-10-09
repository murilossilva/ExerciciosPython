from random import shuffle

def embaralha(palavra):
    random = list(palavra)
    shuffle(random)
    random = ''.join(random)
    return random

palavra = input('Digite uma palavra a ser embaralhada: ')
embaralha(palavra), print(embaralha(palavra).upper())
