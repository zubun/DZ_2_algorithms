#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def random_list():
    import random
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list

def summ_namber(arg):
    # number = input('Введите число: ')
    sum = 0
    # prod = 1
    for f in arg:
        sum += int(f)
        # prod *= int(f)
    # print(f"Сумма цифр числа {number}: {sum}")
    # print(f"Произведение цифр: {number}: {prod}")
    return sum

list_namber = random_list()
#print(list_namber)
max_summ = 0
number = 0
for i in list_namber:
    num = summ_namber(str(i))
    if num > max_summ:
         max_summ = num
         number = i
print(f'Наибольшее число по сумме цифр {number}, сумма = {max_summ}.')