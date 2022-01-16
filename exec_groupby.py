from itertools import groupby, tee

alunos = [
    {'nome':'Murilo','nota':'A'},
    {'nome':'Andressa','nota':'C'},
    {'nome':'Thamyres','nota':'B'},
    {'nome':'Otávio','nota':'C'},
    {'nome':'Kaio','nota':'D'},
    {'nome':'Marcela','nota':'A'},
    {'nome':'Pedro','nota':'D'}
    ]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    
    print(f'Agrupamento: {agrupamento}')
    
    for aluno in va1:
        print(f'Nome do aluno: {aluno["nome"]}')
        
    quantidade = len(list(va2))       

    if quantidade > 1:
        print(f'{quantidade} alunos tiraram nota {agrupamento}')
    else:
        print(f'{quantidade} aluno tirou nota {agrupamento}')
        
    print('-' * 50)
