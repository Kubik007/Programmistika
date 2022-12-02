# Напишите функцию sum_range(start, end), которая суммирует все целые числа
# от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
start = int(input('Введите первое число '))
end = int(input('Введите второе число'))

def sum_range(start, end):
    if start > end:
        start, end = end, start
    k = 0
    for i in range (start, end+1):
        k += i
    return k
print(sum_range(start, end))

