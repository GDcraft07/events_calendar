from config import NUMBER_OF_SLOTS

class Day:
    ''' Класс отдельно взятого дня из календаря '''
    
    def __init__(self, id: int, day: int, month: int, year: int) -> None:
        ''' Инициализация полей класса: id дня, день, месяц и год, а также список всех меротриятий в этот день '''

        self.id = id
        self.day = day
        self.month = month
        self.year = year
        self.events = []


    def add_event(self, event) -> None:
        ''' Добавление мероприятия в список мероприятий '''

        self.events += [event]


    def get_mask(self, venue_id: int) -> list:
        ''' Получение маски занятоски слотов в определенный день и на определенной площадке '''

        day_mask = [0] * NUMBER_OF_SLOTS
        
        for event in self.events:
            if event.venue.id == venue_id:
                day_mask = event.add_event_in_mask(day_mask)

        return day_mask


    def get_day_information(self) -> tuple:
        ''' Возвращает картеж с полями день, месяц и год '''

        return (self.day, self.month, self.year)


    def get_attributes(self) -> dict:
        ''' Возвращает поля класса, которые будут записаны в json файл '''

        return {
            "id": self.id,
            "day": self.day,
            "month": self.month,
            "year": self.year
        }
