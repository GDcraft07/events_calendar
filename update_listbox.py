from tkinter import END
from config import START_TIME_MINUTES


def update_listbox(list_day: list, venue_id: int, date: list, listbox) -> None:
    ''' Обнавления поля со списком всех мероприятий на опредененной площадке в определенный день '''

    listbox.delete(0, END)

    events = []
    
    for i in list_day:
        if i.get_day_information() == date:
            events = i.get_events_on_venue(venue_id)
            break

    if events:
        events.sort(key=lambda event: event.start_id)
        listbox.insert(END, "МЕРОПРИЯТИЯ:")

        for event in events:
            start_event_minutes = event.start_id * 15 + START_TIME_MINUTES
            end_event_minutes = event.end_id * 15 + START_TIME_MINUTES
            listbox.insert(END, f"{event.event_name} от {event.organization.organization_name} c {start_event_minutes // 60}:{"00" if not start_event_minutes % 60 else start_event_minutes % 60} до {end_event_minutes // 60}:{"00" if not end_event_minutes % 60 else end_event_minutes % 60}")

    else:
        listbox.insert(END, "МЕПРОПРИЯТИЙ НЕТУ")
