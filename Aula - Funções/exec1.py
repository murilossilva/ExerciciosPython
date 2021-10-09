def nums_1(n):
    for i in range(n):
        i += 1
        print(f'{str(i) + " "}' * i)

n = input('Digite um número: ')
n = int(n)

nums_1(n)
