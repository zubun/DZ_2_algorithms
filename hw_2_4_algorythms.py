# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = input("Количество элементов: ")
n = int(n)
# первый элемент равен единице
item = 1
# Вводится новая переменная
data = 0
# цикл сделает n итераций
while n > 0:
    # Производится умножение
    data += item
    # выводится текущее значение элемента
    print(item, end=' ')
    # Значение переменной меняется.
    # Оно уменьшается вдвое и изменяет
    # знак на обратный.
    item = item / -2
    # значение n уменьшается на единицу
    n -= 1
print('\n', f'Сумма элементов следующего ряда равна: {data}')

