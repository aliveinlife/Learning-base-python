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
           "выход"
                      ] # Cписок команд

print(f"{tovari}")

def comand(t):      # Функция ввода неверной команды
    g = 0
    for i in t:
        if g == 0:
            print("Неправильно, вот список доступных команд")
            g += 1
        print(f"{i}")
     
    return 0


def list(n):
    for i in n:
         print(f"Товар {i} за: {n[i]}")
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




while True:

    n = 0
 
    protocol = str(input(("Команда? ")).lower().strip())



    if protocol == "":
        e += 1
        if e == 3:
            break
        continue


    for q in comands:

        if protocol == q:
            break

        else:
            n += 1

        if n == 3:
            e += 1
            if e == 3:
                break
            comand(comands)
            break

    if protocol == "добавить":
        add(tovari)
        e = 0

    if protocol == "инфо":
        list(tovari)
        e = 0

    if protocol == "выход":
        break


