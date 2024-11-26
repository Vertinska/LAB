string = input("Введите строку: ")

dot_count = string.count('.')

new_string = string.replace('.', '')

print(f"Изменённая строка: {new_string}")
print(f"Количество удалённых точек: {dot_count}")