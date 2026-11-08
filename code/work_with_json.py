import json


def read_json(file_name: str) -> dict:
    ''' Получаем данные из json-файла '''

    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def edit_json(file_name: str, new_data: dict) -> None:
    ''' Изменяем данные в json-файле '''
    
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)
