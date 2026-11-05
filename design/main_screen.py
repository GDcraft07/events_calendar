from tkinter import *
from tkinter import ttk
from config import HEIGHT, WIDTH, SIZE_SLOT, ROW_COUNT_SLOTS, COLUMN_COUNT_SLOTS, COLORS, TEXT_FONT
from tkcalendar import DateEntry


def main_screen():
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{(root.winfo_screenwidth() - WIDTH) // 2}+{(root.winfo_screenheight() - HEIGHT) // 2}")

    frame_main = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame_main.place(x=0, y=0, height=HEIGHT, width=WIDTH * 5 // 7)
    frame_main.update()

    frame_infromation = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame_infromation.place(x=WIDTH * 5 // 7, y=0, height=HEIGHT, width=WIDTH * 2 // 7)

    frame_work_with_event = ttk.Frame(master=frame_main, borderwidth=1, relief=SOLID)
    frame_work_with_event.place(x=0, y=0, height=frame_main.winfo_height() * 4 // 5, width=frame_main.winfo_width())

    frame_dashboard = ttk.Frame(master=frame_main, borderwidth=1, relief=SOLID)
    frame_dashboard.place(x=0, y=frame_main.winfo_height() * 4 // 5, height=frame_main.winfo_height() // 5, width=frame_main.winfo_width())


    date_entry = DateEntry(master=frame_main)
    date_entry.place(x=13, y=10)


    slots_canvas = Canvas(bg=COLORS["WHITE"], width=(SIZE_SLOT * COLUMN_COUNT_SLOTS), height=(SIZE_SLOT * ROW_COUNT_SLOTS))
    slots_canvas.place(x=13, y=40)
    slots_canvas.update()

    for i in range(ROW_COUNT_SLOTS):
        for j in range(COLUMN_COUNT_SLOTS):
            slots_canvas.create_rectangle(j * SIZE_SLOT, i * SIZE_SLOT, (j + 1) * SIZE_SLOT, (i + 1) * SIZE_SLOT, fill=COLORS["GRAY"], outline=COLORS["BLACK"])


    organization_label = ttk.Label(master=frame_main, text="Организация", font=TEXT_FONT)
    organization_label.place(x=13, y=(slots_canvas.winfo_height() + slots_canvas.winfo_y() + 3))
    organization_label.update()
    
    organization_combobox = ttk.Combobox(master=frame_main, width=26)
    organization_combobox.place(x=13, y=(organization_label.winfo_height() + organization_label.winfo_y() + 2))
    organization_combobox.update()


    password_label = ttk.Label(master=frame_main, text="Пароль", font=TEXT_FONT)
    password_label.place(x=(organization_label.winfo_x() + organization_combobox.winfo_width() + 20), y=organization_label.winfo_y())
    password_label.update()

    password_entry = ttk.Entry(master=frame_main, width=29)
    password_entry.place(x=password_label.winfo_x(), y=(password_label.winfo_height() + password_label.winfo_y() + 1))
    password_entry.update()


    creat_event_button = ttk.Button(master=frame_main, text="Добавить мероприятие")
    creat_event_button.place(x=(password_entry.winfo_x() + password_entry.winfo_width() + 20), y=(password_entry.winfo_y() - 2))
    creat_event_button.update()

    root.mainloop()
