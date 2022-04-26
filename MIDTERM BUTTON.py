from tkinter import *
window = Tk()

window.title("SPECIAL MIDTERM EXAM IN OOP")
window.geometry("500x300")

btn = Button(window, text = "Click to change color", fg = "black", bg = "yellow")
btn.place (x=200, y=150)

window.mainloop()