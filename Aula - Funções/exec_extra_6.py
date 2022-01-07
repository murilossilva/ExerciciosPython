def func_2(*args):
    return args

def func_1(*args):
    return *args, soma(*args), sub(*args)

def soma(*args, valor=50):
    return(sum(args, valor))

def sub(*args):
    total = 0
    for v in args:
        total -= v
    return total

lista = [10, 20, 30, 40]
var = func_2(*lista)
print(func_1(*var))
