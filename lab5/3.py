# Задана множина символів
initial_set = {'c', 'd'}

# Множина голосних латинських літер
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

# Додавання голосних літер до заданої множини
updated_set = initial_set.union(vowels)

# Виведення оновленої множини на екран
print("Задана множина:", initial_set)
print("Множина голосних латинських літер:", vowels)
print("Оновлена множина:", updated_set)