import random


def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Угадайте число (1-100): "))
        attempts += 1
        if guess < number:
            print("Слишком мало!")
        elif guess > number:
            print("Слишком много!")
        else:
            print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток!")
            break


guess_number()