from tkinter import Canvas
from config import COLORS, SIZE_SLOT, COLUMN_COUNT_SLOTS, ROW_COUNT_SLOTS, COUNT_SLOTS
from change_color import change_color


def create_canvas(master, list_day, list_organization, venue_id, date):
    slots_canvas = Canvas(master=master, bg=COLORS["WHITE"], width=(SIZE_SLOT * COLUMN_COUNT_SLOTS), height=(SIZE_SLOT * ROW_COUNT_SLOTS))
    slots_canvas.place(x=13, y=40)
    slots_canvas.update()

    select_slot_ids = [None, []]
    mask = [0] * COUNT_SLOTS

    for i in list_day:
        if i.get_day_information() == date:
            mask = i.get_mask(venue_id)
            break


    for i in range(ROW_COUNT_SLOTS):
        for j in range(COLUMN_COUNT_SLOTS):
            slot_id = slots_canvas.create_rectangle(j * SIZE_SLOT, i * SIZE_SLOT, (j + 1) * SIZE_SLOT, (i + 1) * SIZE_SLOT, fill=COLORS["GRAY"] if not mask[i * COLUMN_COUNT_SLOTS + j] else list_organization[mask[i * COLUMN_COUNT_SLOTS + j] - 1].color, outline=COLORS["BLACK"])

            slots_canvas.tag_bind(slot_id, "<Button-1>", lambda _, slot_id=slot_id, slots_canvas=slots_canvas, select_slot_ids=select_slot_ids, mask=mask, venue_id=venue_id: change_color(slot_id, slots_canvas, select_slot_ids, mask, venue_id))

    return slots_canvas