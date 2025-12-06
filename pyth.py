#Нахождение наибольшего элемента в списке Реализуйте функцию, которая рекурсивно
#находит наибольший элемент в списке.
#Рекурсивное разбиение Создайте функцию, которая рекурсивно разбивает целое число на
#все возможные комбинации меньших чисел,сумма которых равна исходному числу.Например, для числа 4 результатом могут быть
#[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3] и т.д.
import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1,20))

def find_max(lst):
    if len(lst) == 1:
        return lst[0]

    rec_max = find_max(lst[1:])
    return lst[0] if lst[0] > rec_max else rec_max
print(numbers)
print(find_max(numbers))

def get_partitions(n):
    def helper(target, min_val):
        if target == 0:
            return [[]]

        partitions = []

        for i in range(min_val, target + 1):
            for p in helper(target - i, i):
                partitions.append([i] + p)
        return partitions
    result = []
    for i in range(1, n):
        for p in helper(n - i, i):
            result.append([i] + p)

    return result

print(get_partitions(4))