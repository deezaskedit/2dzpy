# 3. Задайте список из n чисел последовательности
#  (1+1/n)**n и выведите на экран их сумму.

def i_num():
    while True:
        try:
            n = int(input('Введите число: '))
            return n
        except:
            print('Неправильный ввод')


def formula(n):
    listt = []
    for i in range(1, n + 1):
        num = ((1 + 1/i) ** i)
        listt.append(round(num,2))
    print(f'Сумма элементов списка - {sum(listt)}')
    return listt
    
print(formula(i_num()))
