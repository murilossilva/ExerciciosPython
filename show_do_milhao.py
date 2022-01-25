print('\n\t\tSeja bem-vindo ao Show do Milhão com Python!\n')
print('Responda cada uma das perguntas com apenas uma alternativa [a,b,c ou d]')

perguntas = {
    'Pergunta 1' : {'pergunta' : 'Qual bicho transmite Doença de Chagas?',
                    'alternativas' :
                    {'a' : 'Moscas',
                     'b' : 'Barata',
                     'c' : 'Pulga',
                     'd' : 'Barbeiro',
                     },
                    'resposta_correta' : 'd'},
    
    'Pergunta 2' : {'pergunta' : 'Qual fruto é conhecido no Norte e Nordeste como "jerimum"?',
                    'alternativas' :
                    {'a' : 'Caju',
                     'b' : 'Abóbora',
                     'c' : 'Chuchu',
                     'd' : 'Coco',
                     },
                    'resposta_correta' : 'b'},
                    
    'Pergunta 3' : {'pergunta' : 'Qual é o coletivo de cães?',
                    'alternativas' :
                    {'a' : 'Matilha',
                     'b' : 'Rebanho',
                     'c' : 'Alcateia',
                     'd' : 'Manada',
                     },
                    'resposta_correta' : 'a'},

    'Pergunta 4' : {'pergunta' : 'Qual é o triângulo que tem todos os lados diferentes?',
                    'alternativas' :
                    {'a' : 'Equilátero',
                     'b' : 'Isóceles',
                     'c' : 'Escaleno',
                     'd' : 'Trapézio',
                     },
                    'resposta_correta' : 'c'},
    
    'Pergunta 5' : {'pergunta' : 'Quem compôs o Hino da Independência?',
                    'alternativas' :
                    {'a' : 'Dom Pedro I',
                     'b' : 'Manuel Bandeira',
                     'c' : 'Castro Alvez',
                     'd' : 'Carlos Gomes',
                     },
                    'resposta_correta' : 'a'},
    
    'Pergunta 6' : {'pergunta' : 'Qual é o antônimo de "malograr"?',
                    'alternativas' :
                    {'a' : 'Perder',
                     'b' : 'Fracassar',
                     'c' : 'Conseguir',
                     'd' : 'Desprezar',
                     },
                    'resposta_correta' : 'c'},
    
    'Pergunta 7' : {'pergunta' : 'Em que país nasceu Carmem Miranda?',
                    'alternativas' :
                    {'a' : 'Brasil',
                     'b' : 'Espanha',
                     'c' : 'Portugal',
                     'd' : 'Argentina',
                     },
                    'resposta_correta' : 'c'},
    
    'Pergunta 8' : {'pergunta' : 'Qual foi o último Presidente do período da ditadura militar no Brasil?',
                    'alternativas' :
                    {'a' : 'Costa e Silva',
                     'b' : 'João Figueiredo',
                     'c' : 'Ernesto Geisel',
                     'd' : 'Emílio Médici',
                     },
                    'resposta_correta' : 'b'},
    
    'Pergunta 9' : {'pergunta' : 'Seguindo a sequência do baralho, qual carta vem depois do dez?',
                    'alternativas' :
                    {'a' : 'Rei',
                     'b' : 'Valete',
                     'c' : 'Nove',
                     'd' : 'Ás',
                     },
                    'resposta_correta' : 'b'},
    
    'Pergunta 10' : {'pergunta' : 'O adjetivo "venoso" está relacionado a?',
                    'alternativas' :
                    {'a' : 'Vela',
                     'b' : 'Vento',
                     'c' : 'Vênia',
                     'd' : 'Veia',
                     },
                    'resposta_correta' : 'd'},
    
    'Pergunta 11' : {'pergunta' : 'Que nome se dá à purificação por meio da água?',
                    'alternativas' :
                    {'a' : 'Abolição',
                     'b' : 'Abnegação',
                     'c' : 'Ablução',
                     'd' : 'Abrupção',
                     },
                    'resposta_correta' : 'c'},
    
    'Pergunta 12' : {'pergunta' : 'Qual montanha se localiza entre a fronteira do Tibet com o Nepal?',
                    'alternativas' :
                    {'a' : 'Monte Everest',
                     'b' : 'Monte Carlo',
                     'c' : 'Monte Fuji',
                     'd' : 'Monte Branco',
                     },
                    'resposta_correta' : 'a'},
    
    'Pergunta 13' : {'pergunta' : 'Em que parte do corpo se encontra a epiglote?',
                    'alternativas' :
                    {'a' : 'Estômago',
                     'b' : 'Pâncreas',
                     'c' : 'Rim',
                     'd' : 'Boca',
                     },
                    'resposta_correta' : 'd'},
    
    'Pergunta 14' : {'pergunta' : 'A compensação por perda é chamada de? ',
                    'alternativas' :
                    {'a' : 'Déficit',
                     'b' : 'Indenização',
                     'c' : 'Indexação',
                     'd' : 'Indébito',
                     },
                    'resposta_correta' : 'b'},
    
    'Pergunta 15' : {'pergunta' : 'Em que dia nasceu e em que dia foi registrado o Presidente Lula?',
                    'alternativas' :
                    {'a' : '6 e 27 de Outubro',
                     'b' : '8 e 27 de Outubro',
                     'c' : '9 e 26 de Outubro',
                     'd' : '7 e 23 de Outubro',
                     },
                    'resposta_correta' : 'a'},
}

print()
respostas_corretas = 0
for pk, pv in perguntas.items():
    print(pv['pergunta'])
    for alt, alt_value in pv['alternativas'].items():
        print(f'[{alt}] - {alt_value}')
    resposta_usuario = input('Qual a alternativa certa? ')
    if resposta_usuario == pv['resposta_correta']:
        print('\nParabéns, sua resposta está correta! xD')
        respostas_corretas += 1
    else:
        print('\nPuxa vida, sua resposta está incorreta! :(')
    print('----------------------------------------------------------')

porcentagem = respostas_corretas / (len(perguntas))
print(f'O seu total de acertos foi de {respostas_corretas} resposta(s) correta(s)!.')
print(f'Você teve um total de {porcentagem * 100:.2f}% acertos.')
