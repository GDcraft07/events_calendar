from config import NUMBER_OF_SLOTS

class Day:
    def __init__(self, id: int, day: int, month: int, year: int) -> None:
        self.id = id
        self.day = day
        self.month = month
        self.year = year
        self.events = []


    def add_event(self, event) -> None:
        self.events += [event]


    def get_mask(self, venue_id: int) -> list:
        day_mask = [0] * NUMBER_OF_SLOTS
        for event in self.events:
            if event.venue.id == venue_id:
                day_mask = event.add_event_in_mask(day_mask)

        return day_mask


    def get_day_information(self) -> tuple:
        return (self.day, self.month, self.year)


    def get_attributes(self) -> dict:
        return {
            "id": self.id,
            "day": self.day,
            "month": self.month,
            "year": self.year
        }
