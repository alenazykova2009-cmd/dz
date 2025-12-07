while True:
    try:
        days = int(input("Введите целое число: "))
        if 1 <= days <= 7:
            break
        else:
            print("Ошибка: Введите число от 1 до 7")
    except ValueError:
        print("Ошибка: Введите целые число")
total_hours = 0
for day in range(1, days + 1):
    while True:
        try:
            hours = float(input(f"Введите кол-во часов учебы задень {day} :"))
            if hours < 0:
                print("Кол-во часов не может быть отрицательным")
            else:
                total_hours += hours
                break
        except ValueError:
            print("Введите числовое значение")

print(f"Общее кол-во часов учебы за неделю: {total_hours}")