def func_2():
    return 10

def func_1(args):
    return args

var = func_1(func_2)
print(var())
