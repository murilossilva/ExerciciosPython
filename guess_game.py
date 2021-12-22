palavra = 'python'
chances = len(palavra)//2
letras_acertadas = []

while True:
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1 or not letra.isalpha():
        print('Isso não vale! Digite apenas uma letra!')
        continue

    if letra in palavra:
        letras_acertadas.append(letra)
        print(f'Parabéns, a letra "{letra}" existe na palavra!')
        print(f'Letras que você acertou: {letras_acertadas}')
    else:
        chances -= 1
        print(f'A letra "{letra}" não está presente na palavra!'
              f' Cuidado, você tem apenas {chances} chance(s)')

    if chances <= 0:
        print(f'\nVocê perdeu todas as suas chances, a palavra era "{palavra}"!')
        break

    palavra_temporaria = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '*'

    print(palavra_temporaria)
    
