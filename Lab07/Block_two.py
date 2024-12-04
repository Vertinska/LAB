import csv

# Функция для чтения и вывода содержимого CSV файла
def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            for key, value in row.items():
                print(f"{key} -> {value}")
            print()

# Функция для вычисления минимального значения по столбцу Score
def min_score(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        scores = [float(row['Year']) for row in reader if row['Year'].isdigit()]
    return min(scores)

# Функция для вычисления максимального значения по столбцу Score
def max_score(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        scores = [float(row['Score']) for row in reader if row['Score'].isdigit()]
    return max(scores)

# Функция для вычисления среднего значения по столбцу Score
def average_score(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        scores = [float(row['Score']) for row in reader if row['Score'].isdigit()]
    return sum(scores) / len(scores) if scores else 0

# Пример использования:
filename = '3.csv'  # Ваш файл CSV

# Вывести содержимое файла в формате Ключ → Значение
print("Содержимое файла в формате 'Ключ → Значение':")
read_csv(filename)

# Вычислить минимальное, максимальное и среднее значение по столбцу Score
#print("\nМинимальное значение по столбцу 'Score':", min_score(filename))
#print("Максимальное значение по столбцу 'Score':", max_score(filename))
#print("Среднее значение по столбцу 'Score':", average_score(filename))
