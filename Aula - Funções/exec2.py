def nums(n):
    for j in range(1,n+1):
        i = 1
        while True:
            print(i, end=' ')
            if i == j:
                break
            i += 1
        print()

n = input('Digite um número: ')
n = int(n)

nums(n)
