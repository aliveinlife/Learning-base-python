from datetime import datetime, date
from finance_data import sdata, ldata

                                                     # Блок инициализации чего либо


data = ldata()


def ifdategood():
    while True:
        datein = input("Дата? (YYYY-MM-DD) -> ").strip()
        try:
            datetime.strptime(datein, "%Y-%m-%d")
            break
        except ValueError:
            print("Ошибка! Введите дату в формате YYYY-MM-DD")
    return datein

def add_record(record_type, data):


    while True:
        category = input("Категория? -> ")
        if category != "":
            break
        else:
            print("Ошибка! Категория должна значить хоть что-то")


    while True:
        try:
            amount = float(input("Кол-во -> "))
            if amount > 0:
                break
            print("Ошибка! Число должно быть положительным!") 
        except ValueError:
            print("Ошибка! Введите число")


    askfordate = input("1. Сегодняшняя дата\n 2. Поставить свою дату. (YYYY-MM-DD)\n ->")
    match askfordate:
        case "1":
            dateindata = date.today().isoformat()
        case "2":
            dateindata = ifdategood()


    askfordescription = input("Добавить описание?(yes/no) -> ").lower().strip()
    if askfordescription == "да" or askfordescription == "yes":
        description = input("Описание? -> ")
    else:
        description = None


    data.append({"id": len(data) + 1, "type": record_type, "amount": amount, "category": category,  "date": dateindata, "description": description })
    

def show_all(data):
    print(f"{'ID':<3} | {'Тип':<7} | {'Сумма':<8} | {'Категория':<10} | {'Дата':<10} | {'Описание'}")
    for rec in data:
        print(f"{rec['id']:<3} | {rec['type']:<7} | {rec['amount']:<8.2f} | {rec['category']:<10} | {rec['date']:<10} | {rec.get('description', '')}")
        

def balance(data):
    total_balance = 0
    for one in data:
        record_type = one["type"]
        match record_type:
            case "income":
               total_balance += one["amount"]
            case "expense":
               total_balance -= one["amount"]
    print(f"Общий баланс -> {total_balance}")


def report_period(data):
    count = 0
    incomeanswear = 0
    expenseanswear = 0
    print("формат YYYY-MM-DD")
    startdate = ifdategood()
    enddate = ifdategood()

    cat_expanses = {}


    for record in data:
        if startdate <= record["date"] <= enddate:
            count += 1
            record_type = record["type"]
            match record_type:
                case "income":
                    incomeanswear = incomeanswear + record["amount"]
                case "expense":
                    cat = record['category']   
                    expenseanswear = expenseanswear + record["amount"]
                    cat_expanses[cat] = cat_expanses.get(cat, 0) + record["amount"]
    if count >= 1:
        print(f"Доходов за период -> {incomeanswear}")
        print(f"Расходов за период -> {expenseanswear}")
        for name, variable in cat_expanses.items():
            print(f"{name} -> {variable}")
        return None
    print("За период нет записей!")

def delete_record(data):
    show_all(data)
    count = 0
    while True:
        try:
            askforid = int(input("Какой id удаляем? "))
            for idplace, checkforid in enumerate(data):
                if askforid == checkforid["id"]:
                    count += 1
                    del data[idplace]
                    print("Запись удалена!")
            if count != 0:
                return None
            print("Запись не найдена")
            return None
        except IndexError:
            print("Ошибка! Введите действительный id")
        except ValueError:
            print("Ошибка! Введите число")


def main(data):
    error = 0
    while True:
        if error == 5:
            print("Блокировка за спам.")
            return None


        task = str(input('''
        1. Добавить доход
        2. Добавить расход
        3. Показать все записи
        4. Показать баланс
        5. Показать отчёт за период (доходы/расходы по категориям)
        6. Удалить запись по ID
        0. Выход
        Команда -> ''')).strip()


        match task:
            case "1":
                rtype = "income"
                add_record(rtype, data)
            case "2":
                rtype = "expense"
                add_record(rtype, data)
            case "3":
                show_all(data)
            case "4":
                balance(data)
            case "5":
                report_period(data)
            case "6":
                delete_record(data)
            case "0":
                return None
            case _:
                print("Ошибка! Вводите число без точки.")
                error += 1
                continue
        error = 0
        sdata(data)


if __name__ == "__main__":
    main(data)
    print("Завершение программы")
    sdata(data)