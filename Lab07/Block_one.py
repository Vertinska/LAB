import pickle
workers = {
    'Иванов': {2018: 50000, 2019: 50000, 2020: 60000, 2021: 55000, 2022: 62000},
    'Петров': {2018: 50000, 2019: 45000, 2020: 66000, 2021: 48000, 2022: 51000},
    'Сидоров': {2018: 74000, 2019: 70000, 2020: 71000, 2021: 72000, 2022: 73000},
    'Кузнецов': {2018: 59000, 2019: 55000, 2020: 56000, 2021: 57000, 2022: 58000},
    'Ковалев': {2018: 51000, 2019: 48000, 2020: 49000, 2021: 50000, 2022: 52000},
    'Лебедев': {2018: 64000, 2019: 60000, 2020: 61000, 2021: 62000, 2022: 63000},
    'Тихонов': {2018: 56000, 2019: 52000, 2020: 53000, 2021: 54000, 2022: 55000},
}
print("Рабочие и их средняя зарплата:")
for worker, salaries in workers.items():
    avg_salary = sum(salaries.values()) / len(salaries)
    print(f"{worker}: {avg_salary:.2f}")

print("\nГод с минимальной суммарной зарплатой для каждого рабочего:")
for worker, salaries in workers.items():
    min_year = min(salaries, key=salaries.get)
    print(f"{worker}: {min_year} с зарплатой {salaries[min_year]}")

min_salary_2019_worker = min(workers.items(), key=lambda item: item[1][2019])
max_salary_2019_worker = max(workers.items(), key=lambda item: item[1][2019])
print(f"\nМинимальная зарплата в 2019 году: {min_salary_2019_worker[0]} - {min_salary_2019_worker[1][2019]}")
print(f"Максимальная зарплата в 2019 году: {max_salary_2019_worker[0]} - {max_salary_2019_worker[1][2019]}")

print("\nРабочие, у которых зарплата в 2018 меньше, чем в 2020 более чем на 10%:")
for worker, salaries in workers.items():
    if salaries[2018] < salaries[2020] * 0.9:
        print(worker)

with open('data.pickle', 'wb') as f:
    pickle.dump(workers, f)

with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

print("\nДанные, загруженные из файла:")
print(loaded_data)



from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as infile:
    text = infile.read()

words = text.split()
word_counts = Counter(words)

most_common_word, most_common_count = word_counts.most_common(1)[0]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f"Слово с наибольшей частотой: '{most_common_word}' (повторяется {most_common_count} раз(а)).")

print(f"Результат записан в 'output.txt': слово '{most_common_word}' с частотой {most_common_count}.")
