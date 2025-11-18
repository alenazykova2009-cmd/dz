import random
#задание 1
print(eval(input("Введите число: ")))
#задане2
list1 = [random.randint(-10,10)for i in range(10)]
list2 = min(list1),max(list1)
negative = 0
positive = 0
zero = 0
for i in (list1):
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1
print(f"""
{list1}
{list2}s
{negative}
{positive}
{zero}
""")