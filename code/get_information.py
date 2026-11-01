from work_with_json import read_json, edit_json
from classes.organization import Organization
from classes.venue import Venue
from classes.day import Day
from classes.event import Event


def get_data(json_link: str) -> tuple[list, list, list, list]:
    ''' Функция проходится по файлу json и формирует классы Python для работы с ними '''
    
    data = read_json(json_link)

    list_organization = []
    list_venue = []
    list_day = []
    list_event = []

    for org in data["organization"]:
        list_organization.append(Organization(org["id"], org["organization_name"], org["color"], org["password"]))

    for venue in data["venue"]:
        list_venue.append(Venue(venue["id"]))

    for day in data["day"]:
        list_day.append(Day(day["id"], day["day"], day["month"], day["year"]))

    for event in data["event"]:
        list_event.append(Event(list_venue[event["venue"]], list_organization[event["organization"]], list_day[event["day"]], event["start_id"], event["end_id"], event["event_name"], event["bio"]))

    empty_data = {
       "organization": [],
        "venue": [],
        "day": [],
        "event": []
    }

    edit_json(json_link, empty_data)

    return (list_organization, list_venue, list_day, list_event)