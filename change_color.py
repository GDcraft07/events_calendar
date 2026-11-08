from config import COLORS
import tkinter
from config import START_END

def change_color(slot_id: int, slots_canvas: tkinter.Canvas, select_slot_ids: list, mask: list, venue_id: int, listbox, events: list) -> list:
    ''' Функция обрабатывающая нажатия на слоты '''
    
    slot_color = slots_canvas.itemcget(slot_id, "fill")

    if slot_color == COLORS["GRAY"]:
        if select_slot_ids[0] == None:
            slots_canvas.itemconfig(slot_id, fill=COLORS["RED"])
            select_slot_ids[0] = True
            select_slot_ids[1].append(slot_id)
            mask[slot_id - 1] = -1

        else:
            if slot_id > select_slot_ids[1][-1]:
                if sum(mask[select_slot_ids[1][-1] + 1:slot_id]) == 0:
                    for i in range(select_slot_ids[1][-1] + 1, slot_id + 1):
                        slots_canvas.itemconfig(i, fill=COLORS["RED"])
                        select_slot_ids[1].append(i)
                        mask[i - 1] = -1
                    select_slot_ids[0] = True

            else:
                if sum(mask[slot_id + 1:select_slot_ids[1][0] - 1]) == 0:
                    for i in range(slot_id, select_slot_ids[1][0]):
                        slots_canvas.itemconfig(i, fill=COLORS["RED"])
                        select_slot_ids[1].append(i)
                        mask[i - 1] = -1
                    select_slot_ids[1] = sorted(select_slot_ids[1])
                    select_slot_ids[0] = False

    elif slot_color == COLORS["RED"]:
        if len(select_slot_ids[1]) == 1:
            slots_canvas.itemconfig(slot_id, fill=COLORS["GRAY"])
            select_slot_ids[0] = None
            select_slot_ids[1] = []
            mask[slot_id - 1] = 0
            START_END[venue_id] = [0, 0]


        else:
            if select_slot_ids[0]:
                for i in range(select_slot_ids[1][0], slot_id):
                    slots_canvas.itemconfig(i, fill=COLORS["GRAY"])
                    select_slot_ids[1].remove(i)
                    mask[i - 1] = 0
                    select_slot_ids[0] = False
            
            else:
                for i in range(slot_id + 1, select_slot_ids[1][-1] + 1):
                    slots_canvas.itemconfig(i, fill=COLORS["GRAY"])
                    select_slot_ids[1].remove(i)
                    mask[i - 1] = 0
                    select_slot_ids[0] = True

    else:
        events.sort(key=lambda x: x.start_id)

        index = 0

        for i in range(0, len(events)):
            if slot_id <= events[i].end_id:
                index = i
                break

        listbox.selection_clear(0, tkinter.END)
        listbox.selection_set(index + 1)

    if select_slot_ids[0] != None:
        START_END[venue_id] = [select_slot_ids[1][0], select_slot_ids[1][-1]]
