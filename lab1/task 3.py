try:
    a = int(input("Введіть ціле число: "))  # Введене число користувачем
    if a != 8:
        print("Будь ласка, введіть число відповідно до варіанту.")
    else:
        # Побудова рисунка
        n = 5

        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                print(j, end="")
            print()

except ValueError:
    print("Некоректний ввід. Неправильне число.")
