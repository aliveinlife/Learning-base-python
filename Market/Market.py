from database import sdata, ldata

# Блок инициализации чего либо

data = ldata()

e = 0                 # Переменная отвечающая за спам

comands = [
           "инфо",
           "добавить",
           "удалить",
           "выход",
                        ] # Cписок команд

# Блок с функциями

def comand(t):      # Функция ввода неверной команды
    g = 0
    for i in t:
        if g == 0:
            print("Вот список доступных команд:\n")
            g += 1
        print(f"{i}")


def spisok(n):                      # Функция показывающая список товаров
    print("")
    for i, o in n.items():
         print(f"{i} за: {o}")
    print("")

def getprice():                     # Функция присваевание цены к товару
    while True:
        a = input("Введите цену: ").strip()
        if a.isdigit():
            return int(a)
        elif a == "назад" or a == "выход":
            return None
        print("\nОшибка!")
        

def add(n):                        # Функция добавление нового товара
    while True:
        a = input("\nВведите название: ").lower().strip()
        if a != "":
            b = getprice()
            if b == None:
                continue
            n[a] = int(b)
            print(f"\nТовар {a} за {b} добавлен!")
            sdata(n)
            return None
        elif a == "выход" or a == "назад":
            return None
        print("Ошибка! Попробуй ещё раз")


def delete(n):                    # Функция удаление
    print("")
    print("Cписок:")
    spisok(n)
    while True:
        print("")
        i = input("Что удалить? ").lower().strip()
        if i in n:
            del n[i]
            sdata(n)
            return None
        elif i == "назад" or i == "выход":
            return None
        else:
            print("Ошибка!")

# Основа

while True:


    comand(comands)                                        # Вывод списка команд
    protocol = str(input(("\nКоманда? ")).lower().strip())   # Спрашиваем команду


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