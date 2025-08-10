def word_count(text):
    words = text.split()
    return len(words)

def main():
    text = input("Введите текст: ")
    count = word_count(text)
    print(f"Количество слов: {count}")
    # Подсчет уникальных слов
    unique_words = len(set(text.lower().split()))
    print(f"Количество уникальных слов: {unique_words}")

main()