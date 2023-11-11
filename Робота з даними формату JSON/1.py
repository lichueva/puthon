import json

#Функція для читання вмісту JSON-файлу
def read_json_file(file_path):
    with open(file_path, 'rt') as file:
        data = json.load(file)
    return data

#Функція для запису в JSON файл
def write_json_file(file_path, data):
    with open(file_path, 'wt') as file:
        json.dump(data, file, indent=2)

#Функція для відображення вмісту JSON-файлу
def display_json_content(file_path):
    data = read_json_file(file_path)
    print(json.dumps(data, indent=2))

#Функція для додавання нового запису в JSON-файл
def add_record(file_path, record):
    data = read_json_file(file_path)
    data.append(record)
    write_json_file(file_path, data)

#Функція для видалення запису з JSON-файлу за певним полем і значенням
def delete_record(file_path, field, value):
    data = read_json_file(file_path)
    data = [record for record in data if record.get(field) != value]
    write_json_file(file_path, data)

#Функція пошуку даних в JSON-файлі за певним полем і значенням
def search_by_field(file_path, field, value):
    data = read_json_file(file_path)
    result = [record for record in data if record.get(field) == value]
    return result

#Функція підрахунку сумарної вартості за тиждень
def calculate_total(file_path):
    data = read_json_file(file_path)
    total_value = 0

    # Consider only the last 5 days
    for day_data in data[-5:]:
        for detail_type, detail_info in day_data.items():
            # Assuming each detail_info has keys 'quantity' and 'unit_price'
            if 'quantity' in detail_info and 'unit_price' in detail_info:
                total_value += detail_info['quantity'] * detail_info['unit_price']
    return total_value

details_data = [
    {
        "day": "Monday",
        "Type1": {"quantity": 100, "unit_price": 5},
        "Type2": {"quantity": 150, "unit_price": 7},
        "Type3": {"quantity": 200, "unit_price": 10},
        "Type4": {"quantity": 120, "unit_price": 8},
        "Type5": {"quantity": 180, "unit_price": 6}
    },
    {
        "day": "Tuesday",
        "Type1": {"quantity": 80, "unit_price": 5},
        "Type2": {"quantity": 120, "unit_price": 7},
        "Type3": {"quantity": 180, "unit_price": 10},
        "Type4": {"quantity": 90, "unit_price": 8},
        "Type5": {"quantity": 150, "unit_price": 6}
    },
    {
        "day": "Wednesday",
        "Type1": {"quantity": 110, "unit_price": 6},
        "Type2": {"quantity": 160, "unit_price": 8},
        "Type3": {"quantity": 220, "unit_price": 12},
        "Type4": {"quantity": 130, "unit_price": 9},
        "Type5": {"quantity": 190, "unit_price": 7}
    },
    {
        "day": "Thursday",
        "Type1": {"quantity": 90, "unit_price": 4},
        "Type2": {"quantity": 130, "unit_price": 6},
        "Type3": {"quantity": 170, "unit_price": 9},
        "Type4": {"quantity": 100, "unit_price": 7},
        "Type5": {"quantity": 160, "unit_price": 5}
    },
    {
        "day": "Friday",
        "Type1": {"quantity": 120, "unit_price": 5},
        "Type2": {"quantity": 170, "unit_price": 7},
        "Type3": {"quantity": 210, "unit_price": 11},
        "Type4": {"quantity": 140, "unit_price": 8},
        "Type5": {"quantity": 200, "unit_price": 6}
    }
]

#Запис даних у JSON-файл
write_json_file("details_data.json", details_data)

while True:
    print("\nВиберіть дію:")
    print("1. Відображення вмісту JSON")
    print("2. Додати новий запис")
    print("3. Видалення запису за полем і значенням")
    print("4. Пошук за полем та значенням")
    print("5. Розрахувати загальну вартість за тиждень")
    print("6. Вихід")

    choice = input("Введіть свій вибір (1-6): ")

    if choice == "1":
        display_json_content("details_data.json")
    
    elif choice == "2":
        new_record = {
    "day": input("Введіть день: "),
    "Type1": {
        "quantity": int(input("Введіть кількість для Type1: ")),
        "unit_price": float(input("Введіть ціну за одиницю для Type1: "))
    },
    "Type2": {
        "quantity": int(input("Введіть кількість для Type2: ")),
        "unit_price": float(input("Введіть ціну за одиницю для Type2: "))
    },
    "Type3": {
        "quantity": int(input("Введіть кількість для Type3: ")),
        "unit_price": float(input("Введіть ціну за одиницю для Type3: "))
    },
    "Type4": {
        "quantity": int(input("Введіть кількість для Type4: ")),
        "unit_price": float(input("Введіть ціну за одиницю для Type4: "))
    },
    "Type5": {
        "quantity": int(input("Введіть кількість для Type5: ")),
        "unit_price": float(input("Введіть ціну за одиницю для Type5: "))
    }
}

        add_record("details_data.json", new_record)
    
    elif choice == "3":
        field = input("Введіть поле для видалення: ")
        value = input("Введіть значення для видалення: ")
        delete_record("details_data.json", field, value)
    
    elif choice == "4":
        field = input("Введіть поле для пошуку: ")
        value = input("Введіть значення для пошуку: ")
        result = search_by_field("details_data.json", field, value)
        print("Результат пошуку:")
        print(json.dumps(result, indent=2))
    
    elif choice == "5":
        total_value = calculate_total("details_data.json")
        print(f"Загальна вартість деталей на один тиждень становить: ${total_value}")
    
    elif choice == "6":
        print("Ви вийшли з програми")
        break
    
    else:
        print("Неправильний вибір. Будь ласка, введіть число від 1 до 6.")