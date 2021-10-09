import random as rd

matriz = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

resp = False

def square():
    global resp
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        resp = True
    else:
        resp = False
    return resp

while resp == False:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for k in range (3):
            random = rd.choice(nums)
            matriz[i][k] = random
            z = nums.index(random)
            nums = nums[z+1:] + nums[:z]
    square()
print(matriz)
