from tkinter import *
from random import *
import time

class Bot:
    def init(self, rect, energy):
        self.coords=None
        self.energy=None
        self.energy_int=None

class Food:
    def init(self):
        self.coords=None

window=Tk()
window.geometry("800x600")
canvas = Canvas(window, width=800, height=600)
bots=[]
coords=[]
food=[]
energy=[]
energy_int=[]

#создание карты
for i in range(20, 640, 20):
    canvas.create_line(0, i, 800, i)
for i in range(20, 840, 20):
    canvas.create_line(i, 0, i, 600)
#===========================================================

#создание ботов
for i in range(64):
    x=randint(0, 40)*20
    y=randint(0, 30)*20
    bots.append(canvas.create_rectangle(x, y, x+20, y+20, fill='blue'))
    energy.append(canvas.create_text(x+10, y+10, text='20', fill='white', ))
    energy_int.append(20)
    coords.append(canvas.coords(bots[i]))
#========================================================
canvas.pack(fill=BOTH)



window.bind('<Right>', right)
window.mainloop()
