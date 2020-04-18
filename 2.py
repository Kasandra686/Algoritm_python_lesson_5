# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


import collections

BASE = 16

HEX_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

num1 = collections.deque(input('Введите первое число ').upper())
num2 = collections.deque(input('Введите второе число ').upper())


def fun_sum(num1, num2):
    num1 = num1.copy()
    num2 = num2.copy()
    mem = 0
    num1 = collections.deque(num1)
    num2 = collections.deque(num2)
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num2.extendleft('0' * (len(num1) - len(num2)))
    res = collections.deque()
    while len(num1) != 0:
        first_num = BIN_NUMBERS[num1.pop()]
        second_num = BIN_NUMBERS[num2.pop()]
        result_num = first_num + second_num + mem
        if result_num >= BASE:
            mem = 1
            result_num -= BASE
        else:
            mem = 0
        res.appendleft(HEX_LIST[result_num])

    if mem == 1:
        res.appendleft('1')

    return ''.join(res)


def fun_multiplication(num1, num2):
    num1 = collections.deque(num1)
    num2 = collections.deque(num2)
    res = collections.deque()
    multiplier = 0
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    num1.reverse()
    for i in range(len(num1)):
        multiplier += HEX_LIST.index(num1[i]) * 16 ** i
    for _ in range(multiplier):
        res = fun_sum(collections.deque(res), collections.deque(num2))
    if not res:
        return 0
    return res



print(f'Сумма равна {fun_sum(num1, num2)}')
print(f'Произведение равно {fun_multiplication(num1, num2)}')

