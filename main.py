# Задача «Сумма цифр»
# Необходимо посчитать сумму четных и нечетных цифр в заданном
# числе.
# Входные параметры: целое число в диапазоне от 0 до 1020
# Результат: два числа через пробел – сумма нечетных и нечетных цифр в
# заданном числе
# Пример:
# Вход – 1234567890
# Результат – 25 20
# Вход – 224466
# Результат – 0 24


def task1(numbers):
    chet = 0
    nechet = 0
    for number in str(numbers):
        if int(number) % 2 == 0:
            chet += int(number)
        else:
            nechet += int(number)
    print(f'{nechet} {chet}')


# Задача «Лесенка»
# Необходимо написать программу, которая выведет на экран лесенку из
# символов # заданного размера.
# Входные параметры: целое число в диапазоне от 1 до 20
# Результат: лесенка заданного размера
# Пример:
# Вход – 10
# Результат – #
##
###
####
#####
######
#######
########
#########
##########

def task2(number):
    a = '{:>%d}' % number
    for x in range(1, number + 1):
        print(a.format('#' * x))




# * Игра «Угадай число»
# Необходимо написать программу, которая будет угадывать загаданное
# человеком число (от 1 до 100).
# Программа совершает попытки угадать число, пользователь отвечает на
# них командами «Больше» (загаданное число больше, чем предложенное
# программой), «Меньше» (загаданное число меньше, чем предложенное
# программой), «Верно» - число угадано, программа завершается.

def task3(start, end):
    if start > end:
        return True

    mid = (start + end) // 2

    print("Загаданное число - ",
          mid, "?", end=" ")
    user = input()
    print(user)

    if user == "Верно" or user == "верно":
        print("Поздравляю! Программа угадала ваше загаданное число!.")
        return False
    elif user == "Больше" or user == "больше":
            return task3(mid + 1, end)
    elif user == "Меньше" or user == "меньше":
            return task3(start, mid - 1)
    else:
        print("Некорректный ввод. Напишите 'Больше'/'Меньше'")
        return task3(start, end)


if __name__ == '__main__':
    # task1(1234567890)
    # task1(224466)
    task2(10)
    # task3(1, 100)