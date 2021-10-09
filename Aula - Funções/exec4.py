def exec4(x):
    if x > 0:
        return 'P'
    else:
        return 'N'

x = input('Digite um número inteiro: ')
x = int(x)

exec4(x)
print(exec4(x))
