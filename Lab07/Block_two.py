import csv

def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            for key, value in row.items():
                print(f"{key} -> {value}")
            print()

def min_score(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        scores = [float(row['Year']) for row in reader if row['Year'].isdigit()]
    return min(scores)

def max_score(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        scores = [float(row["Year"]) for row in reader if row["Year"].isdigit()]
    return max(scores)

def average(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        scores = [float(row['Year']) for row in reader if row['Year'].isdigit()]
    return sum(scores) / len(scores) if scores else 0


filename = "3.csv"

print("Содержимое файла в формате 'Ключ → Значение':")
read_csv(filename)

# Вычислить минимальное, максимальное и среднее значение по столбцу Score
print("\nМинимальное значение по столбцу 'Score':", min_score(filename))
print("Максимальное значение по столбцу 'Score':", max_score(filename))
print("Среднее значение по столбцу 'Score':", average(filename))




import json

def read_json_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def filter_users_by_id(data, id_part):
    filtered_data = [user for user in data if id_part in user.get('id', '')]
    return filtered_data

def save_to_json_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

input_file = 'lab.json'
output_file = 'out.json'
id_part_to_search = 'V59'

try:
    data = read_json_to_dict(input_file)

    filtered_users = filter_users_by_id(data, id_part_to_search)

    unique_users = {user['id']: user for user in filtered_users}.values()

    save_to_json_file(list(unique_users), output_file)

    print(f"Отфильтрованные данные сохранены в файл {output_file}.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
