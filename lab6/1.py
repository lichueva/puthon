# Функція для створення словника даних про потужність двигуна і вартість автомобілів
def create_car_data():
    car_data = {}
    for i in range(1, 11):
        horsepower = int(input(f"Введіть потужність двигуна (к.с.) для автомобіля {i}: "))
        price = float(input(f"Введіть вартість автомобіля {i}: "))
        car_data[i] = {'horsepower': horsepower, 'price': price}
    return car_data

# Функція для виведення на екран всіх значень словника
def display_car_data(car_data):
    for car in car_data:
        print(f"Автомобіль {car}: Потужність: {car_data[car]['horsepower']} к.с., Вартість: {car_data[car]['price']} грн")

# Функція для знаходження загальної вартості автомобілів з потужністю більше 100 к. с.
def total_price_above_100hp(car_data):
    total_price = 0
    for car in car_data:
        if car_data[car]['horsepower'] > 100:
            total_price += car_data[car]['price']
    return total_price

car_data = create_car_data()
display_car_data(car_data)

# Додавання нового запису до словника
new_car_number = max(car_data.keys()) + 1
new_horsepower = int(input(f"Введіть потужність двигуна (к.с.) для нового автомобіля {new_car_number}: "))
new_price = float(input(f"Введіть вартість нового автомобіля {new_car_number}: "))
car_data[new_car_number] = {'horsepower': new_horsepower, 'price': new_price}

display_car_data(car_data)

# Видалення запису зі словника
car_to_delete = int(input("Введіть номер автомобіля для видалення: "))
if car_to_delete in car_data:
    del car_data[car_to_delete]
else:
    print(f"Автомобіль {car_to_delete} не знайдено у словнику.")

display_car_data(car_data)

# Розрахунок загальної вартості автомобілів з потужністю більше 100 к. с.
total_price = total_price_above_100hp(car_data)
print(f"Загальна вартість автомобілів з потужністю більше 100 к. с.: {total_price} грн")
