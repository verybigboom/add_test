def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Тестирование
test_strings = ["радар", "hello", "А роза упала на лапу Азора", "python"]
for s in test_strings:
    if is_palindrome(s):
        print(f"'{s}' - это палиндром")
    else:
        print(f"'{s}' - не палиндром")