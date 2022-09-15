import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webbrowser
# setup Tkinter window
root = tk.Tk()
root.geometry("1000x800")
root.title("Franspai's Python Sandbox")
label = Label(root, text ="Welcome!" ).pack(padx=20, pady=20)
# make a frame to for webpage button
frame = Frame(root)
# geometry
frame.pack()
# create a button function


def button_hyperlink():
    webbrowser.open_new(r"https://franspai.ddns.net")
# button in frame


btn = Button(frame, text ="Visit my website!", command=button_hyperlink)
btn.pack(padx=20, pady=20)


def paint(event):
# coordinates
    x1, y1, x2, y2 = (event.x - 5), (event.y - 5), (event.x + 5), (event.y + 5)
# paint color
    color = "#D559EA"

    w.create_line(x1, y1, x2, y2, fill=color)
# Canvas


w = Canvas(root, width=1000, height=500)

w.bind("<B1-Motion>", paint)

La = Label(root, text="Drag to draw")
La.pack()
w.pack()
# button to close the program
btnk = Button(root, text="Close", command= root.destroy)
btnk.pack(side='top')

root.mainloop()



