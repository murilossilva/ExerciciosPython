def ler_num(num):
    num = str(num).strip()
    return len(num)

num = input("Digite algum número para saber quantos algarismos ele tem: ")
print("O número informado tem", ler_num(num), 'algarismo(s)')
