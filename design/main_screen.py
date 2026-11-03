from tkinter import *
from config import HEIGHT, WIDTH


def main_screen():
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+{(root.winfo_screenwidth() - WIDTH) // 2}+{(root.winfo_screenheight() - HEIGHT) // 2}")

    root.mainloop()


if __name__ == "__main__":
    main_screen()
