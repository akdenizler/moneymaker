from tkinter import *

x = 0


def func(event):
    
    global x 
    x+=1 
    lab.config(text=x)

def funcii(event):
    global x
    x -=1
    lab.config(text=x)

def square(event):
    num = int(form.get())
    lab.config(text = num**2)

window = Tk()
window.geometry("100x100")
window.config(bg="#DDF1D1")

form = Entry(window, width=14, font="Arial, 20", bg="lightyellow")
form2 = Entry(window, width=14, font="Arial, 20", bg="lightblue")


lab = Label(window)
lab.config(font="Arial, 20", text="MagicMathMaster")

#but1 = Button(window, font="Arial, 20", text="Add now!", width=14, height=3, bg="#DDF1D1", fg="magenta")
#but1.bind("<Button-1>", func)

#but2 = Button(window, font="Arial, 20", text="Subtract now!", width=14, height=3, bg="#DDF1D1", fg="blue")
#but2.bind("<Button-1>", funcii)

but3 = Button(window, font="Arial, 20", text="square :D!", width=14, height=3, bg="#DDF1D1", fg="blue")
but3.bind("<Button-1>", square)


lab.pack()
#but1.pack()
#but2.pack()
but3.pack()
form.pack()
form2.pack()

window.mainloop()

