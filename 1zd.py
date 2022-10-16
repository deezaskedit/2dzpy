# 1. Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.


def Sum_Of_Numbers(num):
    sum = 0
    current = 1
    checkIn = (num % 10)
    while checkIn != 0:
        checkIn = (num % 10 ** current) // 10 ** (current - 1)
        sum += checkIn
        current += 1
    return sum

try:
    num = str(float(input('Введите число: ')))
    sec_num = int(num.replace('.', ''))
    print(f'Сумма цифр равна {Sum_Of_Numbers(sec_num)}')
except:
    print('Введите число!')
