def horas(hora,minuto):
    if hora < 12 and hora >= 0 and 0 < minuto < 60:
        if hora == 0:
            print(f'{hora + 12}:{minuto} A')
        else:
            print(f'{hora}:{minuto} A')
    elif hora < 24 and hora >= 12:
        if hora == 12:
            print(f'{hora}:{minuto} P')
        else:
            print(f'{hora - 12}:{minuto} P')
    else:
        print('Informe uma hora que seja válida!')

hora = 0
minuto = 0
print('Olá, seja bem-vindo(a) ao conversor de horas AM/PM!\nCaso queira sair digite 100'
      ' no campo de horas\n')
while hora != 100:
    hora = input('Informe a hora a ser convertida: ')
    hora = int(hora)
    if hora != 100:
        minuto = input('Informe os minutos: ')
        minuto = int(minuto)
        horas(hora,minuto)
