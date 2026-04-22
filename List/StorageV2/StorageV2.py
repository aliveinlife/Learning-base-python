"""

    Сделай так, чтобы программа работала в бесконечном цикле while True.

    Реализуй три команды:

        "инфо" — выводит весь словарь товаров и цен.

        "добавить" — просит имя товара и цену. Обязательно проверь цену через .isdigit()!

        "выход" — завершает программу.

"""
import json

try:
    with open("List/StorageV2/data.json", "r", encoding="utf-8") as f:
        tovari = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tovari = {}

with open("List/StorageV2/data.json", "w", encoding="utf-8") as g:
    json.dump(tovari, g, indent=4, ensure_ascii=False)




e = 0                 # Переменная отвечающая за спам

comands = [
           "инфо",
           "добавить",
           "выход",
           "удалить"
                        ] # Cписок команд


def comand(t):      # Функция ввода неверной команды
    g = 0
    for i in t:
        if g == 0:
            print("Вот список доступных команд")
            g += 1
        print(f"{i}")

def spisok(n):
    for i, o in n.items():
         print(f"Товар {i} за: {o}")


def getprice():
    while True:
        a = input("Введите цену товара: ").strip()
        if a.isdigit():
            return int(a)
        elif a == "назад":
            return None
        print("Ошибка!")


def add(n):
    while True:
        a = input("Введите название товара: ").lower().strip()
        if a != "":
            b = getprice()
            if b == None:
                continue
            n[a] = int(b)
            print(f"Товар {a} за {b} добавлен!")
            with open("List/StorageV2/data.json", "w", encoding="utf-8") as g:
                json.dump(tovari, g, indent=4, ensure_ascii=False)
            return 0
        print("Ошибка! Попробуй ещё раз")


def delete(n):
    i = input("Что удалить? ")
    if i in n:
        del n[i]
    else:
        print("Неправильно")

while True:


    comand(comands)
    protocol = str(input(("Команда? ")).lower().strip())


    if protocol == "":
        e += 1
        if e == 3:
            break
        continue


    if protocol not in comands:
        e += 1
        if e >= 3:
            break
        print("Ошибка!")
        comand(comands)
        continue


    e = 0

    if protocol == "добавить":
        add(tovari)

    if protocol == "инфо":
        spisok(tovari)

    if protocol == "удалить":
        delete(tovari)

    if protocol == "выход":
        with open("List/StorageV2/data.json", "w", encoding="utf-8") as g:
            json.dump(tovari, g, indent=4, ensure_ascii=False)
        break