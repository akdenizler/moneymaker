from tkinter import *

def func():
    lab.config(text='x')

window = Tk()
window.geometry("100x100")

lab = Label(window)
lab.config(font="Arial, 20", text="1")

but1 = Button(window, font="Arial, 20", text="Start", width=14, height=3, bg="green", fg="red")
but1.bind("<Button-1>", func())

lab.pack()
but1.pack()

window.mainloop()

