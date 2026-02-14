class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
    def info(self):
        return f"{self.name} ({self.__class__.__name__}), {self.age} лет, голод: {self.hunger}"
    def feed(self):
        self.hunger = max(0, self.hunger - 5)
        return f"{self.name} покормлен"
    def play(self):
        self.hunger += 3
        return f"Вы поиграли с {self.name}."
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "Гав"
class Cat(Animal):
    def sound(self):
        return "Мяу"
class Bird(Animal):
    def sound(self):
        return "Чикчирик"

animals = [Dog("Шарик", 3), Cat("Васька", 2), Bird("Кеша", 1)]

def show_animals():
    for i, a in enumerate(animals, 1):
        print(i, a.info())
def choose_index(prompt):
    s = input(prompt).strip()
    if not s.isdigit():
        return None
    i = int(s) - 1
    if 0 <= i < len(animals):
        return i
    return None

while True:
    print("Животные в зоопарке:")
    show_animals()
    print("\nЧто хотите сделать?")
    print("1 - Покормить")
    print("2 - Поиграть")
    print("3 - Услышать звук")
    print("4 - Посмотреть инфо")
    print("0 - Выйти")

    choice = input("Введите номер команды: ")
    if choice == "0":
        print("Пока")
        break
    if choice not in {"1", "2", "3", "4"}:
        print("Неверная команда, введите число от 0 до 4")
        continue

    a = choose_index("Введите номер животного (например 1): ")
    if a is None:
        print("Неверный номер животного")
        continue

    animal = animals[a]
    if choice == "1":
        print(animal.feed())
    elif choice == "2":
        print(animal.play())
    elif choice == "3":
        print(animal.sound())
    elif choice == "4":
        print(animal.info())

