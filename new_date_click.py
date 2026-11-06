from create_canvas import create_canvas
from config import START_END

def new_date_click(_, master, list_day, list_organization, number, date_entry, venue_id):
    START_END[venue_id] = [0, 0]
    create_canvas(master, list_day, list_organization, number, list(map(int, str(date_entry.get_date()).split("-"))))