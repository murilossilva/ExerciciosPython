def func_2():
    return 10

def func_1(args):
    return args

var = func_2()
func_1(var)
print(func_1(var))
