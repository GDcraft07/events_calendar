from tkinter import *
from tkinter import ttk
from config import HEIGHT, WIDTH, SIZE_SLOT, ROW_COUNT_SLOTS, COLUMN_COUNT_SLOTS, COLORS, TEXT_FONT, COUNT_SLOTS
from tkcalendar import DateEntry
from pathlib import Path
from change_color import change_color


def main_screen():
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{(root.winfo_screenwidth() - WIDTH) // 2}+{(root.winfo_screenheight() - HEIGHT) // 2}")
    root.title("Бронирование площадок")


    logo = PhotoImage(file=str(Path(__file__).resolve().parent / "logo.png"))
    root.iconphoto(True, logo)

    frame_main = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame_main.place(x=0, y=0, height=HEIGHT, width=WIDTH * 5 // 7)
    frame_main.update()

    frame_infromation = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame_infromation.place(x=WIDTH * 5 // 7, y=0, height=HEIGHT, width=WIDTH * 2 // 7)

    frame_work_with_event = ttk.Frame(master=frame_main, borderwidth=1, relief=SOLID)
    frame_work_with_event.place(x=0, y=0, height=frame_main.winfo_height() * 6 // 7, width=frame_main.winfo_width())
    frame_work_with_event.update()

    frame_dashboard = ttk.Frame(master=frame_main, borderwidth=1, relief=SOLID)
    frame_dashboard.place(x=0, y=frame_main.winfo_height() * 6 // 7, height=frame_main.winfo_height() // 7, width=frame_main.winfo_width())


    notebook = ttk.Notebook(master=frame_work_with_event)
    notebook.place(x=0, y=0, width=frame_work_with_event.winfo_width(), height=frame_work_with_event.winfo_height())

    venues = [ttk.Frame(notebook) for _ in range(5)]


    for number, master in enumerate(venues):
        notebook.add(master, text=f"Площадка №{number + 1}")

        
        date_entry = DateEntry(master=master)
        date_entry.place(x=13, y=10)


        slots_canvas = Canvas(master=master, bg=COLORS["WHITE"], width=(SIZE_SLOT * COLUMN_COUNT_SLOTS), height=(SIZE_SLOT * ROW_COUNT_SLOTS))
        slots_canvas.place(x=13, y=40)
        slots_canvas.update()

        select_slot_ids = [None, []]
        mask = [0] * COUNT_SLOTS

        for i in range(ROW_COUNT_SLOTS):
            for j in range(COLUMN_COUNT_SLOTS):
                slot_id = slots_canvas.create_rectangle(j * SIZE_SLOT, i * SIZE_SLOT, (j + 1) * SIZE_SLOT, (i + 1) * SIZE_SLOT, fill=COLORS["GRAY"], outline=COLORS["BLACK"])

                slots_canvas.tag_bind(slot_id, "<Button-1>", lambda _, slot_id=slot_id, slots_canvas=slots_canvas, select_slot_ids=select_slot_ids, mask=mask: change_color(slot_id, slots_canvas, select_slot_ids, mask))


        organization_label = ttk.Label(master=master, text="Организация", font=TEXT_FONT)
        organization_label.place(x=13, y=(slots_canvas.winfo_height() + slots_canvas.winfo_y() + 3))
        organization_label.update()
        
        organization_combobox = ttk.Combobox(master=master, width=26)
        organization_combobox.place(x=13, y=(organization_label.winfo_height() + organization_label.winfo_y() + 2))
        organization_combobox.update()


        password_label = ttk.Label(master=master, text="Пароль", font=TEXT_FONT)
        password_label.place(x=(organization_label.winfo_x() + organization_combobox.winfo_width() + 20), y=organization_label.winfo_y())
        password_label.update()

        password_entry = ttk.Entry(master=master, width=29)
        password_entry.place(x=password_label.winfo_x(), y=(password_label.winfo_height() + password_label.winfo_y() + 1))
        password_entry.update()


        creat_event_button = ttk.Button(master=master, text="Добавить мероприятие")
        creat_event_button.place(x=(password_entry.winfo_x() + password_entry.winfo_width() + 20), y=(password_entry.winfo_y() - 2))


    root.mainloop()


if __name__ == "__main__":
    main_screen()