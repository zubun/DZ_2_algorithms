# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
a = int(input(' Введите первое число'))
b = int(input(' Введите второе число'))

n = 1
for i in range(a, b+1):
    if n % 10 == 0:
        print(f'{i}:{chr(i)} ')
    else:
        print(f'{i}:{chr(i)} ', end='')
    n += 1
