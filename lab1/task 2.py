distance = 10  # Початкова відстань в перший день
totalDistance = 0  # Загальна відстань, яку спортсмен пробіг

days = 1  # Лічильник днів

while totalDistance < 50:
    totalDistance += distance
    distance *= 1.1  # Збільшуємо відстань на 10% для наступного дня
    days += 1

print("Спортсмен подолає 50 км за", days, "днів")