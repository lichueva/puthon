# Розмір масиву
rows = 7
cols = 7

# Створення двовимірного масиву та заповнення його значеннями
array = [[7 - j for j in range(cols)] for i in range(rows)]

# Виведення масиву на екран
for row in array:
    print("".join(map(str, row)))
