import requests
import json

url = "https://restcountries.com/v3.1/lang/{language}"

def get_countries_by_language(language):
    response = requests.get(url.format(language=language))
    return response.json()

languages = ['spanish', 'portuguese', 'german']
countries_info = []

for lang in languages:
    countries = get_countries_by_language(lang)
    for country in countries:
        area = country.get('area', 0)
        if area > 100000:
            countries_info.append({
                'name': country['name']['common'],
                'capital': country.get('capital', [None])[0],
                'language': lang,
                'area': area,
                'population': country.get('population', 0),
                'flag': country['flags']['png']
            })

with open('results.json', 'w') as json_file:
    json.dump(countries_info, json_file, indent=4)

print("Информация о странах сохранена в файле results.json.")

max_area_countries = {lang: None for lang in languages}
for country in countries_info:
    lang = country['language']
    if max_area_countries[lang] is None or country['area'] > max_area_countries[lang]['area']:
        max_area_countries[lang] = country

for lang, country in max_area_countries.items():
    if country:
        print(f"Страна с наибольшей площадью на языке {lang}: {country['name']} с площадью {country['area']}")

for country in max_area_countries.values():
    if country:
        flag_url = country['flag']
        response = requests.get(flag_url)
        if response.status_code == 200:
            with open(f"{country['name']}_flag.png", 'wb') as flag_file:
                flag_file.write(response.content)