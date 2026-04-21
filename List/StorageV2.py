"""

    Сделай так, чтобы программа работала в бесконечном цикле while True.

    Реализуй три команды:

        "инфо" — выводит весь словарь товаров и цен.

        "добавить" — просит имя товара и цену. Обязательно проверь цену через .isdigit()!

        "выход" — завершает программу.

"""


tovari = {}           # Список с товарами
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
            print("Неправильно, вот список доступных команд")
            g += 1
        print(f"{i}")
     
    return 0


def spisok(n):
    for i, o in n.items():
         print(f"Товар {i} за: {o}")
    return 0


def add(n):
    a = input("Введите название товара: ").lower().strip()
    b = input("Введите цену товара: ").strip()
    if b.isdigit():
        n[a] = int(b)
        print(f"Товар {a} за {b} добавлен!")
    else:
        print("Ошибка!")
    return 0

def delete(n):
    i = input("Что удалить? ")
    if i in n:
        del n[i]
    else:
        print("Неправильно")

while True: 
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
        break


    