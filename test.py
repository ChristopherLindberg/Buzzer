from tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END, str(i))
    
listbox.xview(2)
    
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)
scrollbar.
mainloop()