from code.classes.event import Event
from create_canvas import create_canvas
from tkinter import END, messagebox
from config import START_END, COLORS


def add_event(venue, organization, day, start_id: int, end_id: int, event_name: str, password: str, list_event: list, master, list_day: list, list_organization: list, password_entry, name_event_entry, listbox) -> None:
    if organization == None:
        messagebox.showerror(title="ОШИБКА", message="ВЫБЕРЕТЕ ОРГАНИЗАЦИЮ")
        return

    if not organization.check_password(password):
        messagebox.showerror(title="ОШИБКА", message="НЕПРАВИЛЬНЫЙ ПАРОЛЬ")
        password_entry.delete(0, END)
        return

    if (start_id == 0 and end_id == 0):
        messagebox.showerror(title="ОШИБКА", message="ВЫБЕРЕТЕ СЛОТЫ ПРОВЕДЕНИЯ МЕРОПРИЯТИЯ")
        return

    new_event = Event(venue, organization, day, start_id - 1, end_id, event_name)
    list_event.append(new_event)
    START_END[venue.id] = [0, 0]

    password_entry.delete(0, END)
    name_event_entry.delete(0, END)
    create_canvas(master, list_day, list_organization, venue.id, day.get_day_information(), listbox)
