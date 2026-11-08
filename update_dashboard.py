from datetime import datetime, date
from tkinter import END
from config import START_TIME_MINUTES, COUNT_SLOTS


def update_dashboard(root, dashboard, list_day: list, fisrt_start: bool, its_main_start) -> None:
    time, mili = str(datetime.now().time()).split(".")
    mili = int(mili) // 1000
    hour, minute, second = map(int, time.split(":"))    
    slot = (hour * 60 + minute - START_TIME_MINUTES) // 15
    row_ids = dashboard.get_children()
    day = False

    if row_ids:
        for i in row_ids:
            dashboard.delete(i)

    for i in list_day:
        if i.get_day_information() == [date.today().year, date.today().month, date.today().day]:
            day = i
            break

    if day and 0 <= slot < COUNT_SLOTS:
        events_now = [""] * 5
        events_15_min = [""] * 5
        events_30_min = [""] * 5
        
        for event in day.events:
            if event.start_id <= slot < event.end_id:
                events_now[event.venue.id] = event.event_name

            if event.start_id <= slot + 1 < event.end_id:
                events_15_min[event.venue.id] = event.event_name

            if event.start_id <= slot + 2 < event.end_id:
                events_30_min[event.venue.id] = event.event_name
        
        dashboard.insert("", END, values=("В процессе", *events_now))
        dashboard.insert("", END, values=(f"Через {15 - minute % 15} минут", *events_15_min))
        dashboard.insert("", END, values=(f"Через {30 - minute % 15} минут", *events_30_min))

    else:
        dashboard.insert("", END, values=("В процессе", "", "", "", "", ""))
        dashboard.insert("", END, values=(f"Через {15 - minute % 15} минут","", "", "", "", ""))
        dashboard.insert("", END, values=(f"Через {30 - minute % 15} минут", "", "", "", "", ""))

    if its_main_start:
        root.after(60000 if not fisrt_start else 60000 - (second * 1000 + mili), lambda: update_dashboard(root, dashboard, list_day, True, True))
