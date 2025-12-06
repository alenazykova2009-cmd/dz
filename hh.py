def show_quote():
    text = """
    “Don't let the noise of others' opinions
     drown out your own inner voice.”
                                Steve Jobs)
"""
    print(text)
show_quote()

def show_odds(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i)
show_odds(3, 10)


def draw_line(length, direction, symbol):
    if direction == "горизонталь":
        print(symbol * length)
    elif direction == "вертикаль":
        for _ in range(length):
            print(symbol)


draw_line(15, "горизонталь", "*")
draw_line(5, "вертикаль", "*")


def max_four(a, b, c, d):
    return max(a, b, c, d)

result = max_four(10, 40, 1, 0)
print(f"Максимальное число: {result}")

def sum_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total
print(sum_range(1,15))

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(8))
print(is_prime(11))


def number_math(number):
    if number < 100000 or number > 999999:
        return False

    digit1 = number // 100000
    digit2 = (number // 10000) % 10
    digit3 = (number // 1000) % 10
    digit4 = (number // 100) % 10
    digit5 = (number // 10) % 10
    digit6 = number % 10

    return (digit1 + digit2 + digit3) == (digit4 + digit5 + digit6)
print(number_math(123420))
print(number_math(723422))