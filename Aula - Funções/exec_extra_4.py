def fizzbuzz(n):
    n = int(n)
    if n % 5 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

n = ''
while not n.isnumeric():
    n = input('Insira um número inteiro para começar o programa: ')

fizzbuzz(n)
print(fizzbuzz(n))
