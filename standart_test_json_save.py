from code.classes.organization import Organization
from code.classes.venue import Venue
from code.save_information import save_data
from code.classes.day import Day
from code.classes.event import Event

orgs = [
    Organization(0, "Тинькофф банк", "#00FF00", "12345678", True), 
    Organization(1, "Альфа банк", "#0000FF", "1234", True),
    Organization(2, "Сбербанк", "#00FFF0", "qwerty", True),
    Organization(3, "Точка банк", "#F0FF00", "....", True),
    Organization(4, "ФПИ Банк", "#FF00FF", "nowkie", True)
]

venue = [Venue(i) for i in range(5)]

save_data("C:/Users/GDcraft/Desktop/events_calendar/code/full_information.json", orgs, venue, [], [])