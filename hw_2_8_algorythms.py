# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# Функция "random_list" для создания рандомного "списка" значений.
def random_list():
    import random
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list, par_1, par_2


list_namber = random_list()
#print(list_namber)
n = int(input(f'Введите число количество повторений которого необходимо посчитать. Число должно быть в пределах от {list_namber[1]} до {list_namber[2]}: '))
counter = 0
for i in list_namber[0]:
    if i == n:
        counter +=1
print(f'Введеное вами число {n} повторяется в последлвательности {list_namber[0]} {counter} раз.')