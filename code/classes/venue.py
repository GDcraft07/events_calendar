class Venue:
    ''' Класс отдельной площадки '''
    def __init__(self, id: int) -> None:
        ''' Инициализация полей класса: id площадки '''

        self.id = id
        self.events = []


    def add_event(self, event) -> None:
        ''' Добавление мероприятия в список мероприятий '''

        self.events += [event]


    def get_attributes(self) -> dict:
        ''' Возвращает поля класса, которые будут записаны в json файл '''

        return {
            "id": self.id
        }
