def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не вдалося відкрити")
        return None
    else:
        print("Файл", file_name, "відкрито")
        return file

def process_and_write(input_file, output_file, target_length):
    try:
        input_file = open_file(input_file, "r")
        output_file = open_file(output_file, "w")

        if input_file is not None and output_file is not None:
            for line in input_file:
                #Залишаємо лише цифри у рядку
                digits_only = ''.join(filter(str.isdigit, line))
                
                #Доповнюємо рядок до заданої довжини пробілами
                padded_line = digits_only.ljust(target_length)

                #Записуємо оброблений рядок у вихідний файл
                output_file.write(padded_line + '\n')

            print("Обробка і запис в", output_file.name, "завершено")

    finally:
        #Закриття файлів
        if input_file:
            input_file.close()
        if output_file:
            output_file.close()

def print_file_contents(file_name):
    file = open_file(file_name, "r")

    if file is not None:
        print("Вміст", file_name + ":")
        for line in file:
            print(line.strip())  #Видаляємо символи у кінці нового рядка
        print("Файл", file_name, "закрито")
        file.close()

# a)Створюємо текстовий файл TF11_1 із символьних рядків однакової довжини
file11_1_name = "TF11_1.txt"
with open_file(file11_1_name, "w") as file_11_1:
    strings_to_write = ["270pyt", "324hon", "687txt"]
    for string in strings_to_write:
        file_11_1.write(string + '\n')
print("Файл", file11_1_name, "створено")

# b)Обробляємо і записуємо в TF11_2
file11_2_name = "TF11_2.txt"
target_length = 10
process_and_write(file11_1_name, file11_2_name, target_length)

# c)Виводимо вміст TF11_2
print_file_contents(file11_2_name)