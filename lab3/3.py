# Задане речення
sentence = input("Введіть речення: ")

# Розділення речення на слова
words = sentence.split()

# Пошук і виведення першого слова, яке розпочинається на 'к'
found_word = None

for word in words:
    if word.startswith('к') or word.startswith('К'):
        found_word = word
        break

if found_word:
    print(f"Знайдене слово, що починається на 'к': {found_word}")
else:
    print("У заданому реченні немає слів, які починаються на 'к'.")
