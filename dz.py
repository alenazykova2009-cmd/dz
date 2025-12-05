import random

list1 = []
for _ in range(20):
    list1.append(random.randint(-20,20))

negative_num = 0
chet_num =0
nechet_num = 0
for num in list1:
    if num < 0:
        nechet_num += num
    if num % 2 == 0:
        chet_num += num
    if num % 2 != 0:
        nechet_num += num
index3 = 1
for i in range(len(list1)):
    if i % 3 == 0:
        index3 *= list1[i]

min_index = list1.index(min(list1))
max_index = list1.index(max(list1))

start = min(min_index, max_index)
end = max(min_index, max_index)

prod = 1
if end - start > 1:
    for i in range(start + 1, end):
        prod *= list1[i]
    else:
        prod = 0

positive_indices = [i for i, x in enumerate (list1) if x > 0]
sum_between_positive = sum(list1[positive_indices[0] + 1:positive_indices[-1]])

print(f"""Исходный список: {list1}
Сумма отрицательных: {negative_num}
Сумма четных: {chet_num}
Сумма нечетных: {nechet_num}
Произведение элементов индексами кратными 3: {index3}
Произведение между min и mах: {prod}
Сумма между первым и последним положительными: {sum_between_positive}""")

list2 = [random.randint(-30, 30) for _ in range(20)]
even_list = []
odd_list = []
negative_list = []
positive_list = []

for num in list2:
    if num % 2 == 0:
        even_list.append(num)
    if num % 2 != 0:
        odd_list.append(num)
    if num < 0:
        negative_list.append(num)
    if num > 0:
        positive_list.append(num)

print(f"""Исходный список: {list2}
Четные числа: {even_list}
Нечетные числа: {odd_list}
Отрицательные числа: {negative_list}
Положительные числа: {positive_list}""")

