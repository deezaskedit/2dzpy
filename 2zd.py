def array_fact(num):
    arrayy = [1]*num
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            arrayy[i - 1] *= j
    return arrayy
try:
    num = int(input('Введите число: '))
    print(array_fact(num))
except:
    print('Введите целое число!:')
