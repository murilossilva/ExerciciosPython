import re
from itertools import count

def remove_caracteres_especiais(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    cnpj_copia = cnpj[:-2]
    return contadores(cnpj_copia)


def contadores(cnpj_copia):
    if len(cnpj_copia) == 12:
        contador_1 = count(start = 5, step = -1)
    else:
        contador_1 = count(start = 6, step = -1)
    contador_2 = count(start = 9, step = -1)
    return multiplica_algarismos(cnpj_copia, contador_1, contador_2)


def multiplica_algarismos(cnpj_copia, contador_1, contador_2):
    lista_com_resultados = []
    tamanho_cnpj = len(cnpj_copia)
    
    for algarismo_cnpj, contador in zip(cnpj_copia, contador_1):
        if contador >= 2:
            multiplicacao = int(algarismo_cnpj) * contador
            lista_com_resultados.append(multiplicacao)
            
    if tamanho_cnpj == 12:        
        for algarismo_cnpj, contador in zip(cnpj_copia[4:], contador_2):
            if contador >= 2:
                multiplicacao = int(algarismo_cnpj) * contador
                lista_com_resultados.append(multiplicacao)
                
    else:
        for algarismo_cnpj, contador in zip(cnpj_copia[5:], contador_2):
            if contador >= 2:
                multiplicacao = int(algarismo_cnpj) * contador
                lista_com_resultados.append(multiplicacao)
                
    return formula(sum(lista_com_resultados), cnpj_copia)


def formula(lista_com_resultados, cnpj_copia):
    digito = 11 - (lista_com_resultados % 11)
    
    if digito > 9:
        digito = 0
    else:
        pass
    
    cnpj_copia = cnpj_copia + str(digito)
    
    if len(cnpj_copia) == 13:
        return contadores(cnpj_copia)
    else:
        return cnpj_copia


if __name__ == '__main__':
    cnpj = input('Digite um cnpj para saber se ele é válido ou não: ')
    cnpj_copia = remove_caracteres_especiais(cnpj)
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    print('É válido' if cnpj == cnpj_copia else 'Não é válido')
    
    
    
    
    

    
