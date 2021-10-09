def dataExt(dia, mes, ano):
    lista_de_mes = ["Janeiro", "Fevereiro", "Março",
                    "Abril", "Maio", "Junho",
                    "Julho", "Agosto", "Setembro",
                    "Outubro", "Novembro", "Dezembro"]

    print(f'{dia} de {lista_de_mes[int(mes) - 1]} de {ano}')

dia, mes, ano = input('Informe a data no formato DD/MM/AAAA: ').split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

while dia > 31 or dia < 1:
    dia = input('Informe um dia válido: ')
    dia = int(dia)

while mes > 12 or mes < 1:
    mes = input('Informe um mês válido: ')
    mes = int(mes)

while ano < 0 or ano > 9999:
    ano = input('Informe um ano válido: ')
    ano = int(ano)
    
dataExt(dia, mes, ano)
