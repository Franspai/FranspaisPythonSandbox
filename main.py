import webbrowser
import tkinter as tk
from tkinter import *
from PIL import Image
# setup Tkinter window
root = tk.Tk()
root.geometry("1000x670")
root.title("Franspai's Python Sandbox")
root.configure(bg='white')

# make a frame to for webpage button
frame = Frame(root)
# geometry
frame.pack(side=TOP)


L = tk.Label(root, font=('Helvetica', 15, 'bold'), text="Welcome!", bg="white")
L.pack(side=TOP)

# definition for bg changer
light = PhotoImage(file="switchD.png")
dark = PhotoImage(file="switchl.png")
# resize image function


switch_value = True

def toggle():
    global switch_value
    if switch_value:
        switch.config(image=dark, activebackground="black", background="black", fg="white")

        # change window color
        root.config(bg="black")
        L.config(bg="black", fg="white")
        La.config(bg="black", fg="white")
        w.config(bg="black")
        switch_value = False

    else:
        switch.config(image=light, bg="white", activebackground="white")

        # Change back to light
        root.config(bg="white")
        L.config(bg="white", fg="black")
        La.config(bg="white", fg="black")
        w.config(bg="white")
        switch_value = True


switch = Button(root, image=light, bg="white", command=toggle)
switch.pack()

def paint(event):
# coordinates
    x1, y1, x2, y2 = (event.x - 4), (event.y - 4), (event.x + 4), (event.y + 4)
# paint color
    color = "#D559EA"

    w.create_line(x1, y1, x2, y2, fill=color)
# Canvas


w = Canvas(root, width=1000, height=500, bg="white")

w.bind("<B1-Motion>", paint)

La = tk.Label(root, text="Drag to draw", bg="white")
La.pack()
w.pack()
# create a button function


def button_hyperlink():
    webbrowser.open_new(r"https://franspai.ddns.net")


btn = Button(root, text="Visit my website!", command=button_hyperlink)
btn.pack(side=TOP)
# button to close the program
btnk = Button(root, text="Close", command=root.destroy)
btnk.pack(side=BOTTOM, pady=2)

root.mainloop()



