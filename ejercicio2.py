import tkinter
from tkinter import ttk

window = tkinter.Tk()

selected = tkinter.StringVar()
series = ['The 100', "Games of Thrones", "Cosmos", "La chica nueva", "The Good Doctor"]
list_items_series = tkinter.Variable(value=series)

label = ttk.Label(text="Selecciona tus series favoritas")
label.pack(padx=10, pady=10, anchor=tkinter.W)

list_selector = tkinter.Listbox(listvariable=list_items_series, selectmode=tkinter.MULTIPLE, height=5)
list_selector.pack(padx=10, pady=10, anchor=tkinter.W)

window.mainloop()
