from tkinter import *
from tkinter import ttk
from config import HEIGHT, WIDTH, TEXT_FONT, COUNT_VENUES, START_END, FONT_INFORMATION
from tkcalendar import DateEntry
from pathlib import Path
from code.get_information import get_data
from add_event import add_event
from create_canvas import create_canvas
from add_day_to_list import add_day_to_list
from code.save_information import save_data
from new_date_click import new_date_click 
from datetime import datetime
from update_listbox import update_listbox
from update_dashboard import update_dashboard


def main():
    ''' Основаная функция, в которой собирается весь проект воедино и отрисовывается дизайн '''
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{(root.winfo_screenwidth() - WIDTH) // 2}+{(root.winfo_screenheight() - HEIGHT) // 2}")
    root.title("Бронирование площадок")
    root.resizable(False, False)


    list_organization, list_venue, list_day, list_event = get_data(Path("code").absolute() / "full_information.json")


    logo = PhotoImage(file=str(Path(__file__).resolve().parent / "logo.png"))
    root.iconphoto(True, logo)


    frame_main = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame_main.place(x=0, y=0, height=HEIGHT, width=WIDTH * 5 // 7)
    frame_main.update()

    frame_infromation = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame_infromation.place(x=WIDTH * 5 // 7, y=0, height=HEIGHT, width=WIDTH * 2 // 7)

    frame_work_with_event = ttk.Frame(master=frame_main, borderwidth=1, relief=SOLID)
    frame_work_with_event.place(x=0, y=0, height=frame_main.winfo_height() * 93 // 120, width=frame_main.winfo_width())
    frame_work_with_event.update()

    frame_dashboard = ttk.Frame(master=frame_main, borderwidth=1, relief=SOLID)
    frame_dashboard.place(x=0, y=frame_main.winfo_height() * 93 // 120, height=frame_main.winfo_height() * 27 // 120, width=frame_main.winfo_width())
    frame_dashboard.update()


    listbox_information = Listbox(master=frame_infromation, justify=CENTER, height=frame_infromation.winfo_height(), font=FONT_INFORMATION)
    listbox_information.pack(fill=X)


    notebook = ttk.Notebook(master=frame_work_with_event)
    notebook.place(x=0, y=0, width=frame_work_with_event.winfo_width(), height=frame_work_with_event.winfo_height())


    style = ttk.Style()
    style.configure("Treeview", rowheight=(frame_dashboard.winfo_height() - 26) // 3, font=FONT_INFORMATION)

    dashboard_treeview = ttk.Treeview(master=frame_dashboard, columns=("timing", "venue_1", "venue_2", "venue_3", "venue_4", "venue_5"))
    dashboard_treeview.place(x=0, y=0, width=frame_dashboard.winfo_width(), height=frame_dashboard.winfo_height())

    dashboard_treeview.column("#0", width=0, stretch=NO)
    dashboard_treeview.column("timing", width=frame_dashboard.winfo_width() // 6)
    for i in range(5):
        dashboard_treeview.column(f"venue_{i + 1}", width=frame_dashboard.winfo_width() // 6)

    dashboard_treeview.heading("timing", text="")
    for i in range(5):
        dashboard_treeview.heading(f"venue_{i + 1}", text=f"Площадка №{i + 1}")


    venues = [ttk.Frame(notebook) for _ in range(COUNT_VENUES)]


    for number, master in enumerate(venues):
        notebook.add(master, text=f"Площадка №{number + 1}")

        
        date_entry = DateEntry(master=master, mindate=datetime.now())
        date_entry.place(x=13, y=10)
        date_entry.bind("<<DateEntrySelected>>", lambda _, master=master, list_day=list_day, list_organization=list_organization, number=number, date_entry=date_entry, venue_id=number, listbox=listbox_information: new_date_click(_, master, list_day, list_organization, number, date_entry, venue_id, listbox))

        slots_canvas = create_canvas(master, list_day, list_organization, number, list(map(int, str(date_entry.get_date()).split("-"))), listbox_information)

        organization_label = ttk.Label(master=master, text="Организация", font=TEXT_FONT)
        organization_label.place(x=13, y=(slots_canvas.winfo_height() + slots_canvas.winfo_y() + 3))
        organization_label.update()
        
        organization_combobox = ttk.Combobox(master=master, width=15, values=[org.organization_name for org in list_organization], state="readonly")
        organization_combobox.place(x=13, y=(organization_label.winfo_height() + organization_label.winfo_y() + 2))
        organization_combobox.update()

        password_label = ttk.Label(master=master, text="Пароль", font=TEXT_FONT)
        password_label.place(x=(organization_label.winfo_x() + organization_combobox.winfo_width() + 20), y=organization_label.winfo_y())
        password_label.update()

        password_entry = ttk.Entry(master=master, width=20, show="*")
        password_entry.place(x=password_label.winfo_x(), y=(password_label.winfo_height() + password_label.winfo_y() + 1))
        password_entry.update()

        name_event_label = ttk.Label(master=master, text="Название мероприятия", font=TEXT_FONT)
        name_event_label.place(x=(password_label.winfo_x() + password_entry.winfo_width() + 20), y=organization_label.winfo_y())
        name_event_label.update()

        name_event_entry = ttk.Entry(master=master, width=20)
        name_event_entry.place(x=name_event_label.winfo_x(), y=(name_event_label.winfo_height() + name_event_label.winfo_y() + 1))
        name_event_entry.update()


        def accept_click(password_entry=password_entry, organization_combobox=organization_combobox, date_entry=date_entry, master=master, name_event_entry=name_event_entry):
            ''' Обработчик нажатия на кнопку '''
            
            password = password_entry.get()
            name_event = name_event_entry.get()

            add_event(list_venue[notebook.index(notebook.select())], list_organization[organization_combobox.current()] if organization_combobox.current() != -1 else None, add_day_to_list(date_entry.get_date(), list_day), *START_END[notebook.index(notebook.select())], name_event, password, list_event, master, list_day, list_organization, password_entry, name_event_entry, listbox_information, root, dashboard_treeview)
            update_listbox(list_day, notebook.index(notebook.select()), list(map(int, str(date_entry.get_date()).split("-"))), listbox_information)

        creat_event_button = ttk.Button(master=master, text="Добавить мероприятие", command=accept_click)
        creat_event_button.place(x=(name_event_entry.winfo_x() + name_event_entry.winfo_width() + 20), y=(name_event_entry.winfo_y() - 2))


    update_listbox(list_day, notebook.index(notebook.select()), list(map(int, str(date_entry.get_date()).split("-"))), listbox_information)
    notebook.bind("<<NotebookTabChanged>>", lambda _: update_listbox(list_day, notebook.index(notebook.select()), list(map(int, str(date_entry.get_date()).split("-"))), listbox_information))

    update_dashboard(root, dashboard_treeview, list_day, True, True)

    root.mainloop()

    save_data(Path("code").absolute() / "full_information.json", list_organization, list_venue, list_day, list_event)


if __name__ == "__main__":
    main()
