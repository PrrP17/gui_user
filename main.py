from tkinter import *
from tkinter import colorchooser


def click():
  color = colorchooser.askcolor()
  print(color)

window = Tk()

window.geometry("500x500")

button = Button(text='wtf' ,command=click)
button.pack()

window.mainloop()

