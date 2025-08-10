def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()  # Переход на новую строку после каждой строки таблицы

print("Таблица умножения 10x10:")
multiplication_table()