from .config import SALT
from hashlib import sha256


class Organization:
    ''' Класс организации, которая проводит мероприятие '''

    def __init__(self, id: int, organization_name: str, color: str, password: str, is_not_hash: bool=False) -> None:
        ''' Инициализация полей класса: id организации, название организации, цвет организации и пароль '''

        self.id = id
        self.organization_name = organization_name
        self.events = []
        self.color = color
        self.password = self.hash_password(password) if is_not_hash else password


    def add_event(self, event) -> None:
        ''' Добавление мероприятия в список мероприятий '''

        self.events += [event]


    def get_attributes(self) -> dict:
        ''' Возвращает поля класса, которые будут записаны в json файл '''

        return {
            "id": self.id,
            "organization_name": self.organization_name, 
            "color": self.color,
            "password": self.password
        }


    @staticmethod
    def hash_password(password: str) -> str:
        ''' Статический метод для хэширования пароля '''

        return sha256((SALT + password).encode("utf-8")).hexdigest()


    def check_password(self, password: str) -> bool:
        ''' Проверка пароля '''

        return self.hash_password(password) == self.password
