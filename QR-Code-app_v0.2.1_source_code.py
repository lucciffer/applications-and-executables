import tkinter as tk
import pyqrcode
from pyqrcode import QRCode
import png
import datetime

win = tk.Tk()
win.title("QRify")
win.geometry("400x200")
photo = tk.PhotoImage(file = "qr1.png")
win.iconphoto(False, photo)
win.configure(bg="#00efff")

OptionList = [
".png",
".svg"
]
#app by lucciffer
def qrcodegenerator():
    text = entry.get()
    site = text
    val = formatoption.get()
    url = pyqrcode.create(site)
    saveas = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    if val ==".png":
        url.png('QR' + saveas + '.png',scale = 8)
    elif val ==".svg":
        url.svg('QR' + saveas + '.svg',scale = 8)
    label = tk.Label(win, text="SUCCESS!",bg = "black",fg ="#00ff00")
    label.grid(row=4,column=0)

#app by lucciffer
label = tk.Label(win, text="Generate QR code for: ",bg ="#00efff")
label.grid(row=0,column=0)
entry = tk.Entry(win)
entry.grid(row=0,column=1)

blanklabel = tk.Label(win,text = "",bg = "#00efff") #blank line 0
blanklabel.grid(row=1,column=1)

button = tk.Button(win,text="Generate QR",bg="black",fg="white",font="courier 10",command=qrcodegenerator)
button.grid(row=2,column=0)

formatoption = tk.StringVar(win)
formatoption.set(OptionList[0])
optiondisplay = tk.Label(win,text="choose format:",bg="#00efff")
optiondisplay.grid(row=1,column=0)
opt = tk.OptionMenu(win, formatoption, *OptionList)
opt.config(width=5, font=('courier 10', 12))
opt.grid(row=1,column=1)


quit_button = tk.Button(win, text = "Exit app",bg="red",fg="yellow", command = win.quit)
quit_button.grid(row=3,column=0)

blanklabel2 = tk.Label(win,text = "",bg = "#00efff") #blank line 1
blanklabel2.grid(row=4,column=1)
blanklabel3 = tk.Label(win,text = "",bg = "#00efff") #blank line 2
blanklabel3.grid(row=5,column=1)


luccy = tk.Label(win, text = "App by Lucciffer",bg = "#00efff",fg = "#000000")
luccy.grid(row = 6,column = 1)
win.mainloop()
#app by lucciffer
