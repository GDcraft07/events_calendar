from create_canvas import create_canvas

def new_date_click(_, master, list_day, list_organization, number, date_entry):
    create_canvas(master, list_day, list_organization, number, list(map(int, str(date_entry.get_date()).split("-"))))