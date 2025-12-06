import secrets
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    alphabet = ""
    if use_lowercase:
        alphabet += string.ascii_lowercase
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_special:
        alphabet += string.punctuation

    password = ""
    for i in range(length):
        password += secrets.choice(alphabet)
    return password

def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False


def generate_unique_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special):
    unique_passwords = set()
    while len(unique_passwords) < count:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        unique_passwords.add(password)
    return list(unique_passwords)

if __name__ == "__main__":
    pwd = generate_password(10, True, True, True, True)
    print("Сгенерируемый пароль:", pwd)

    if check_password_strength(pwd):
        print("Пароль надежный")
    else:
        print("Пароль не надежный")


    unique_passwords = generate_unique_passwords(3, 8, True, True, True, True)
    print("Уникальные пароли:", unique_passwords)