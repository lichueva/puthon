import matplotlib.pyplot as plt
import numpy as np
import csv

def read_csv(file_path):
    data = []
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file, delimiter=',', quotechar=',')
            for row in reader:
                row_data = [elem.replace('"', '') for elem in row]
                data.append(row_data)
    except Exception as err:
        print(err)
        exit(0)
    return data

def plot_graph(x, y1, y2, label1, label2, xlabel, ylabel):
    plt.plot(x, y1, 'b', label=label1, lw=3)
    plt.plot(x, y2, 'r', label=label2, lw=3)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def plot_bar(x, y, label, xlabel, ylabel):
    plt.bar(x, y, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def main():
    file_path = "1.csv"
    data = read_csv(file_path)

    x = data[0][2:]
    y1 = [round(float(value), 5) for value in data[1][2:]]
    y2 = [round(float(value), 5) for value in data[2][2:]]

    print("Виберіть дію:\n1. Зображення графіка для двох країн\n"\
        "2. Зображення стовпчастої діаграми для однієї країни")

    while True:
        choice = input("Вибір: ")
        if choice == '1':
            plot_graph(x, y1, y2, data[1][1], data[2][1], "Рік", "Показник")
            break
        elif choice == '2':
            print("Виберіть країну:\n1 - США\n2 - Україна")
            ch = input("Вибір: ")
            if ch == '1':
                plot_bar(x, y1, data[int(ch)][1], "Рік", "Показник")
            elif ch == '2':
                plot_bar(x, y2, data[int(ch)][1], "Рік", "Показник")
            else:
                print("Помилка. Спробуйте ще")
            break
        else:
            print("Помилка. Спробуйте ще")

if __name__ == "__main__":
    main()
