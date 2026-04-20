#
# Словари
#
# Задание 1
# Спросить у пользователя какой продукт он ищет и вывести его с ценой на экран

stock = {
    "яблоки": 150,
    "груши": 200,
    "чипсы": 80
}

while True:
    question = str(input("Product you want to know price? "))
    for i in stock:
        if question == i:
            print(stock[i])
    end = str(input("Это всё что вы хотели узнать? "))
    if end != "да":
        continue
    break