import numpy as np
import matplotlib.pyplot as plt

def Y(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)

#значення x [1, 7] з кроком 0.1
x_values = np.linspace(1, 7, 100)
y_values = Y(x_values)

#побудова графіка
plt.plot(x_values, y_values, linestyle='-', color='pink', linewidth=2, label='Y(x)')

#позначення осей
plt.xlabel('X')
plt.ylabel('Y')

#назва графіка
plt.title('Графік функції Y(x) = 5*sin(10*x)*sin(3*x)/(x^(1/2))')

#легенда
plt.legend()

#відображення графіка
plt.show()