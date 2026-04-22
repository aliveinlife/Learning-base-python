import json

"""
# Словарь
tovari = {
    "яблоки": 100,
    "груши": 150,
    "сливы": 80
}
"""

# Записываем его в файл
with open("List/Reading_files/how_to_read.json", "r", encoding="utf-8") as f:
# Теперь нам нужен не .txt а .json
    data = json.load(f)
print(f"{data}")


    # dump — берет объект и «дампит» его в файл
    #json.dump(tovari, f, indent=4, ensure_ascii=False)
    # json - обращение к библеотеке. .dump функция которая переписывает словарь (tovari название словаря. f это файл indent=4 это чтоб мы по человечески видели внутренности ensure_ascii=false за это тоже означает
#print("Данные успешно упакованы в JSON!")

