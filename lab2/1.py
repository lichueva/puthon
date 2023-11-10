import math
# Функція для обчислення змінної z
def calculate_z(x):
    if x >= 1:
        print("x повинно бути менше 1")
        return
    z = math.exp(math.sqrt(x)) / math.sqrt(1 - x)
    return z
# Введення числа x від користувача
x = float(input("Введіть число x: "))
# Виклик функції calculate_z та виведення результату
result_z = calculate_z(x)
if result_z is not None:
    print(f"Результат обчислення z: {result_z}")
# Введення цілого невід'ємного числа N з перевіркою
while True:
    N = int(input("Введіть ціле невід'ємне число N: "))
    if N < 0:
        print("N повинно бути невід'ємним числом. Спробуйте ще раз.")
    else:
        break
# Функція для обчислення добутку в залежності від парності N
def calculate_product(N):
    product = 1
    if N % 2 == 1:  # N - непарне
        for i in range(1, N+1, 2):
            product *= i
    else:  # N - парне
        for i in range(2, N+1, 2):
            product *= i
    return product
# Виклик функції calculate_product та виведення результату
result_product = calculate_product(N)
print(f"Результат обчислення добутку: {result_product}")
