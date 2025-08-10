import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Генерация и вывод пароля
for _ in range(5):
    print(f"Сгенерированный пароль: {generate_password(16)}")