# def sum_sum():
#     stop = ("w")
#     number_summ_all = 0
#     while stop != ("q"):
#         number_summ = []
#         line = input("введите строку: ")
#         number_str = []
#         number_str = line.split()
#         st = 0
#         st = number_str.count("q")
#         if st >0:
#             # number_str.index("q")
#             number_int = list(map(int, number_str[0: number_str.index("q")]))
#             # number_str.remove("q")
#             # number_int = list(map(int, number_str))
#             number_summ = sum(number_int)
#             number_summ_all += number_summ
#             return number_summ_all
#         number_int = list(map(int,number_str))
#         number_summ = sum(number_int)
#         number_summ_all += number_summ
#         stop = input(f"Сумма всех значений равна: {number_summ_all}. Если желаете продолжить введите w, для завршения введите q:")
#     return number_summ_all
#
#
# summ = sum_sum()
# print(f"Сумма введеных значений равна: {summ}.")
#
# a = input('Введите трехзначное число')
# match list(a):
#     case a1, a2, a3:
#         print(int(a1) + int(a2) + int(a3))
#         print(int(a1) * int(a2) * int(a3))
#     case _:
#         print('Вы ввели неверное значение.')

#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.
stop = ("w")
qw = (1)
while stop != (0):
    calculator = input('Введите через пробел: Число_1 Число_2 Знак операции (Пример: 5 6 + ). Для выхода из программы вместо знака операции введите "0".')
    match list(calculator.split()):
        case a, b, sign:
            if sign == '+':
                (print(f'Сумма чисел равна {int(a) + int(b)}.'))
            elif sign == '-':
                print(f'Разность чисел равна {int(a) - int(b)}.')
            elif sign == '*':
                print(f'Произведение чисел равно {int(a) * int(b)}.')
            elif sign == '/':
                if int(b) == 0:
                    print('На ноль делить нельзя.')
                else:
                    print(f'Частное чисел равно {int(a) / int(b)}.')
            elif sign == '0':
                print(f'Вы вышли из прогрммы.')
                qw = 0
            else:
                print(f'Вы ввели неверное значение знака операции. Попробуйте еще раз.')
        case _:
                print('Вы ввели неверное значение.')
    
    stop = qw
