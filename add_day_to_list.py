from code.classes.day import Day


def add_day_to_list(date_information, list_day: list):
    ''' Функция, которая возвращает класс дня который нам нужен из списка или создает его, если такого дня нету '''
    normal_date = list(map(int, str(date_information).split("-")))

    for i in list_day:
        if i.get_day_information() == normal_date:
            return i

    if not list_day:
        day = Day(0, normal_date[-1], normal_date[1], normal_date[0])
    else:
        day = Day(list_day[-1].id + 1, normal_date[-1], normal_date[1], normal_date[0])

    list_day.append(day)

    return day
