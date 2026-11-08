from create_canvas import create_canvas
from config import START_END
from update_listbox import update_listbox


def new_date_click(_, master, list_day: list, list_organization: list, number: int, date_entry, venue_id: int, listbox) -> None:
    ''' Переключает на новый день после нажатия в календаре '''
    
    date = list(map(int, str(date_entry.get_date()).split("-")))
    update_listbox(list_day, venue_id, date, listbox)
    START_END[venue_id] = [0, 0]
    create_canvas(master, list_day, list_organization, number, date, listbox)
