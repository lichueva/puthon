def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def print_list(arr):
    for item in arr:
        print(item, end=" ")
    print()
# Приклад використання функції:
my_list = [51, 13, 22, 74, 1, 56, 27]
print("Список перед сортуванням:")
print_list(my_list)
bubble_sort(my_list)
print("Список після сортування бульбашкою:")
print_list(my_list)
