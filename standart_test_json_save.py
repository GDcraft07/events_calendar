from code.classes.organization import Organization
from code.classes.venue import Venue
from code.save_information import save_data
from code.classes.day import Day
from code.classes.event import Event

orgs = [
    Organization(0, "Тинькофф", "#00FF00", "12345678", True), 
    Organization(1, "Альфа", "#0000FF", "1234", True),
    Organization(2, "Сбер", "#00FFF0", "321", True),
    Organization(3, "Точка банк", "#F0FF00", "432", True),
    Organization(4, "ФПИ Банк", "#FF00FF", "435", True)
]

venue = [Venue(i) for i in range(5)]

days = [
    Day(0, 5, 11, 2026),
    Day(1, 6, 11, 2026),
    Day(2, 7, 11, 2026)
]

events = [
    Event(venue[0], orgs[0], days[1], 11, 15, "Kosta", "")
]

save_data("C:/Users/GDcraft/Desktop/events_calendar/code/full_information.json", orgs, venue, days, events)