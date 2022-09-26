import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import webbrowser
# setup Tkinter window
root = tk.Tk()
root.geometry("1000x620")
root.title("Franspai's Python Sandbox")
root.configure(bg='white')

# make a frame to for webpage button
frame = Frame(root)
# geometry
frame.pack(side=TOP)


L = tk.Label(root, font=('Helvetica', 15, 'bold'), text="Welcome!", bg="white")
L.pack(side=TOP)

# definition for bg changer
light = PhotoImage(file=switchl.png)
dark = PhotoImage(file=switchD.png)

switch_value = True

def toggle():
    global switch_value
    if switch_value:
        switch.config(image=dark, activebackground="black", background="black", fg="white")

        # change window color
        root.config(bg="black")
        L.config(bg="black", fg="white")
        La.config(bg="black", fg="white")
        w.config(bg="black", fg="white")
        switch_value = False

    else:
        switch.config(image=light, bg="white", activebackground="white", fg="black")

        # Change back to light
        root.config(bg="white")
        L.config(bg="white", fg="black")
        La.config(bg="white", fg="black")
        w.config(bg="white", fg="black")
        switch_value = True


switch = Button(root, image=light, bd=0, command=toggle)


def paint(event):
# coordinates
    x1, y1, x2, y2 = (event.x - 5), (event.y - 5), (event.x + 5), (event.y + 5)
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



