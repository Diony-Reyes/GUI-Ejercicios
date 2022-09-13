import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)

os_selected = tkinter.StringVar()

label = ttk.Label(window, text='Seleciona un Sistema Operativo')
label.grid(column=0, row=0, padx=10, pady=5)

label_2 = ttk.Label(window, text='Sistema Operativo seleccionado:')
label_2.grid(column=0, row=1, padx=10, pady=0)

label_result = ttk.Label(window, textvariable=os_selected)
label_result.grid(column=0, row=2, padx=10, pady=0)

clear_button = ttk.Button(window, text='Limpiar', command=lambda: os_selected.set(""))
clear_button.grid(column=0, row=3, padx=10, pady=5)

windows_option = ttk.Radiobutton(window, text="Windows", value="Windows", variable=os_selected)
windows_option.grid(column=1, row=0, padx=10, pady=10)

macos_option = ttk.Radiobutton(window, text="macOS", value="macOS", variable=os_selected)
macos_option.grid(column=1, row=1, padx=10, pady=10)

linux_option = ttk.Radiobutton(window, text="Linux", value="Linux", variable=os_selected)
linux_option.grid(column=1, row=2, padx=10, pady=10)

msdos_option = ttk.Radiobutton(window, text="MS DOS", value="MS DOS", variable=os_selected)
msdos_option.grid(column=1, row=3, padx=10, pady=10)

amigaos_option = ttk.Radiobutton(window, text="AmigaOS", value="AmigaOS", variable=os_selected)
amigaos_option.grid(column=1, row=4, padx=10, pady=10)

beos_option = ttk.Radiobutton(window, text="BeOS", value="BeOS", variable=os_selected)
beos_option.grid(column=1, row=5, padx=10, pady=10)

window.mainloop()
