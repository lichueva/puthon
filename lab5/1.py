def split_list(lst, index):
    if index < 0 or index >= len(lst):
        print("Помилка: вказаний індекс за межами списку або менше 0.")
        return None

    first_list = lst[:index]
    second_list = lst[index:]

    return first_list, second_list

# Отримуємо індекс від користувача
try:
    split_index = int(input("Введіть індекс для розбиття списку: "))
except ValueError:
    print("Помилка: введіть ціле число для індексу.")
else:
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]

    result = split_list(my_list, split_index)
    if result is not None:
        first_half, second_half = result
        print("Перший список:", first_half)
        print("Другий список:", second_half)
