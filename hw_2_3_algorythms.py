# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = list(input('Введите натуральное число: '))
number.reverse()
i = ''.join(number)
print(i)