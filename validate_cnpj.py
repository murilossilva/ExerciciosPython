import re
from itertools import count

def remove_caracteres_especiais(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def sequencia(cnpj):
    try:
        sequencia = cnpj[0] * len(cnpj)
        if sequencia == cnpj:
            print('Números em sequência. CNPJ inválido!')
        else:
            return False
    except Exception as error:
        pass


def validacao(cnpj):
    cnpj = remove_caracteres_especiais(cnpj)
    
    if sequencia(cnpj):
        return False
    
    cnpj_copia = cnpj[:-2]
    return contadores(cnpj_copia)


def contadores(cnpj_copia):
    
    #  cria o contador para verificar o primeiro dígito
    if len(cnpj_copia) == 12:
        contador_1 = count(start = 5, step = -1)

    #  cria o contador para verificar o segundo dígito
    else:
        contador_1 = count(start = 6, step = -1)
        
    contador_2 = count(start = 9, step = -1)
    
    return multiplica_algarismos(cnpj_copia, contador_1, contador_2)


#  função que irá multiplicar os índices
def multiplicacao(lista_com_resultados, algarismo, contador):
    multiplica = int(algarismo) * contador
    return lista_com_resultados.append(multiplica)


def multiplica_algarismos(cnpj_copia, contador_1, contador_2):
    lista_com_resultados = []
    tamanho_cnpj = len(cnpj_copia)
    
    for algarismo_cnpj, contador in zip(cnpj_copia, contador_1):
        if contador >= 2:
            multiplicacao(lista_com_resultados, algarismo_cnpj, contador)
            
    #  laço for para o primeiro dígito         
    if tamanho_cnpj == 12:        
        for algarismo_cnpj, contador in zip(cnpj_copia[4:], contador_2):
            if contador >= 2:
                multiplicacao(lista_com_resultados, algarismo_cnpj, contador)
                
    #  laço for para o segundo dígito            
    else:
        for algarismo_cnpj, contador in zip(cnpj_copia[5:], contador_2):
            if contador >= 2:
                multiplicacao(lista_com_resultados, algarismo_cnpj, contador)
                
    return formula(sum(lista_com_resultados), cnpj_copia)


def formula(lista_com_resultados, cnpj_copia):
    digito = 11 - (lista_com_resultados % 11)    
    digito = digito if digito <= 9 else 0
    
    cnpj_copia += str(digito)

    #  realiza a chamada recursiva para o segundo dígito
    if len(cnpj_copia) == 13:
        return contadores(cnpj_copia)

    #  encerra a cascata de funções e retorna o cnpj a ser comparado com o colocado no input
    else:
        return cnpj_copia


if __name__ == '__main__':
    while True:
        cnpj = input('Digite um cnpj para saber se ele é válido ou não: ')
        cnpj_copia = validacao(cnpj)
        cnpj = re.sub(r'[^0-9]', '', cnpj)
        print('É válido' if cnpj == cnpj_copia else 'Não é válido')

