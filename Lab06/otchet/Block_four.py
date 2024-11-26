num1 = int(input("Введите количество элементов в массиве: "))
arr1 = []
print(f"Введите {num1} элементов массива:")
for i in range(num1):
    score = int(input(f"{i+1} элемент массива: "))
    arr1.append(score)

max_element=max(arr1)
max_index = arr1.index(max_element)

print(f"Максимальный элемент: {max_element}")
print(f"Порядковый номер максимального элемента: {max_index + 1}")


num2 = int(input("Введите количество элементов в массиве: "))
arr2 = []
print(f"Введите {num2} элементов массива:")
for i in range(num2):
    score = int(input(f"{i+1} элемент массива: "))
    arr2.append(score)

odd_numbers = [num for num in arr2 if num % 2 != 0]

if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Массив нечётных чисел в порядке убывания:", odd_numbers)
else:
    print("В массиве нет нечётных чисел.")
