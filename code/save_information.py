from .work_with_json import read_json, edit_json

def save_data(json_link: str, list_organization: list, list_venue: list, list_day: list, list_event) -> None:
    ''' Функция сохраняет поля классов в json-файл '''

    data = read_json(json_link)

    for org in list_organization:
        data["organization"].append(org.get_attributes())

    for venue in list_venue:
        data["venue"].append(venue.get_attributes())


    for day in list_day:
        data["day"].append(day.get_attributes())

    for event in list_event:
        data["event"].append(event.get_attributes())

    edit_json(json_link, data)
