from database import sdata, ldata

data = ldata()


e = 0                 # Переменная отвечающая за спам

comands = [
           "инфо",
           "добавить",
           "удалить",
           "выход",
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
        elif a == "назад" or a == "выход":
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
            sdata(data)
            return None
        elif a == "выход" or a == "назад":
            return None
        print("Ошибка! Попробуй ещё раз")


def delete(n):
    while True:
        for u in n:
            print(f"{u}")
        i = input("Что удалить? ").lower().strip()
        if i in n:
            del n[i]
            sdata(data)
            return None
        elif i == "назад" or i == "выход":
            return None
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
        add(data)

    if protocol == "инфо":
        spisok(data)

    if protocol == "удалить":
        delete(data)

    if protocol == "выход":
        sdata(data)
        break