from code.classes.event import Event
from create_canvas import create_canvas


def add_event(venue, organization, day, start_id: int, end_id: int, event_name: str, password: str, list_event: list, master, list_day: list, list_organization: list) -> None:
    if not organization.check_password(password):
        return None

    new_event = Event(venue, organization, day, start_id - 1, end_id, event_name)
    list_event.append(new_event)

    create_canvas(master, list_day, list_organization, venue.id, day.get_day_information())
