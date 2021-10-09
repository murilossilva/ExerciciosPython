def somaImposto(taxaImposto, custo):
    valor_final = custo + (custo * taxaImposto * 0.01)
    return valor_final

taxaImposto = input('Informe a taxa de imposto em porcentagem. Ex.: 27.5 \n')
taxaImposto = float(taxaImposto)
custo = input('Qual o custo do produto sem a taxa de imposto? ')
custo = float(custo)

somaImposto(taxaImposto, custo)

print('O valor final é de R$',somaImposto(taxaImposto, custo))
    
