from tkinter import Canvas
from config import COLORS, SIZE_SLOT, COLUMN_COUNT_SLOTS, ROW_COUNT_SLOTS, COUNT_SLOTS, START_TIME_MINUTES
from change_color import change_color


def create_canvas(master, list_day: list, list_organization: list, venue_id: int, date: list, listbox) -> Canvas:
    slots_canvas = Canvas(master=master, bg=COLORS["WHITE"], width=(SIZE_SLOT * COLUMN_COUNT_SLOTS), height=(SIZE_SLOT * ROW_COUNT_SLOTS))
    slots_canvas.place(x=13, y=40)
    slots_canvas.update()

    select_slot_ids = [None, []]
    mask = [0] * COUNT_SLOTS
    events = []

    for i in list_day:
        if i.get_day_information() == date:
            mask = i.get_mask(venue_id)
            events = i.get_events_on_venue(venue_id)
            break


    for i in range(ROW_COUNT_SLOTS):
        for j in range(COLUMN_COUNT_SLOTS):
            slot_id = slots_canvas.create_rectangle(j * SIZE_SLOT, i * SIZE_SLOT, (j + 1) * SIZE_SLOT, (i + 1) * SIZE_SLOT, fill=COLORS["GRAY"] if not mask[i * COLUMN_COUNT_SLOTS + j] else list_organization[mask[i * COLUMN_COUNT_SLOTS + j] - 1].color, outline=COLORS["BLACK"])

            slots_canvas.tag_bind(slot_id, "<Button-1>", lambda _, slot_id=slot_id, slots_canvas=slots_canvas, select_slot_ids=select_slot_ids, mask=mask, venue_id=venue_id, listbox=listbox, events=events: change_color(slot_id, slots_canvas, select_slot_ids, mask, venue_id, listbox, events))

    for i in range(ROW_COUNT_SLOTS):
        for j in range(COLUMN_COUNT_SLOTS):
            slot_time = START_TIME_MINUTES + (i * COLUMN_COUNT_SLOTS + j) * 15
            slots_canvas.create_text(j * SIZE_SLOT + 14, i * SIZE_SLOT + 10, text=f"{slot_time // 60}:{"00" if not slot_time % 60 else slot_time % 60}", font=("Arial", 7))

    return slots_canvas
