class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position

    def get_position(self):
        return self._position

    def display_info(self):
        return f"Имя: {self._name}, Возраст: {self._age}, Должность: {self._position}"


class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self._team = []

    def add_to_team(self, employee):
        if employee not in self._team:
            self._team.append(employee)
            return True
        return False

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} (Менеджер)"

    def display_team(self):
        if not self._team:
            return "Команда пуста"
        team_info = [f"  - {emp.display_info()}" for emp in self._team]
        return "Команда:\n" + "\n".join(team_info)


def main():
    employees = []

    while True:
        print("\nУчет сотрудников")
        print("1. Добавить сотрудника")
        print("2. Назначить сотрудника в команду менеджера")
        print("3. Просмотреть всех сотрудников")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Введите имя: ").strip()
            try:
                age = int(input("Введите возраст: ").strip())
            except ValueError:
                print("Ошибка: возраст должен быть числом!")
                continue

            position = input("Введите должность: ").strip()

            if position.lower() == "менеджер":
                emp = Manager(name, age, position)
            else:
                emp = Employee(name, age, position)

            employees.append(emp)
            print(f"Сотрудник {name} добавлен!")

        elif choice == "2":
            if not employees:
                print("Ошибка: нет сотрудников!")
                continue

            manager_name = input("Введите имя менеджера: ").strip()
            employee_name = input("Введите имя сотрудника: ").strip()

            manager = None
            employee = None

            for emp in employees:
                if emp.get_name() == manager_name and isinstance(emp, Manager):
                    manager = emp
                if emp.get_name() == employee_name and not isinstance(emp, Manager):
                    employee = emp

            if not manager:
                print("Ошибка: менеджер не найден!")
            elif not employee:
                print("Ошибка: сотрудник не найден или является менеджером!")
            else:
                if manager.add_to_team(employee):
                    print(f"Сотрудник {employee_name} добавлен в команду {manager_name}")
                else:
                    print("Сотрудник уже в команде")

        elif choice == "3":
            if not employees:
                print("Список сотрудников пуст")
            else:
                print("\n=== Список всех сотрудников ===")
                for emp in employees:
                    print(emp.display_info())
                    if isinstance(emp, Manager):
                        print(emp.display_team())

        elif choice == "4":
            print("Программа завершена")
            break

        else:
            print("Ошибка: неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()