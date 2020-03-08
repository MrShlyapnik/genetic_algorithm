from tkinter import *
from random import *
import time

def right(event):

    global bots
    global canvas
    global coords
    global food
    global energy
    global energy_int
    global food_coords
    global die
    global die_coords

    stoped=0
    coords=[]
    delete=[]
    i=0
    if len(bots)<=8:
        pass
    else:
        while i<len(bots):
            print(i)

            side=randint(1, 4)
            pos=canvas.coords(bots[i])
            x1=pos[0]
            y1=pos[1]
            x2=pos[2]
            y2=pos[3]
            if side==1:
                if y1-20<0:
                    stoped=1
                    # canvas.delete(bots[i])
                    # bots[i]=canvas.create_rectangle(x1, 780, x2, 600)
                else:
                    canvas.delete(energy[i])
                    energy_int[i]-=1

                    canvas.move(bots[i], 0, -20 )
                    # if energy_int[i]==0:
                    #     canvas.delete(bots[i])
                    #     bots = bots[:i] + bots[i + 1:]
                    #     energy = energy[:i] + energy[i + 1:]
                    #     energy_int = energy_int[:i] + energy_int[i + 1:]
                    #     coords = coords[:i] + coords[i + 1:]
                    # else:
                    #     energy[i] = canvas.create_text(canvas.coords(bots[i])[0]+10, canvas.coords(bots[i])[1]+10, text=str(energy_int[i]), fill='white')
                    #
                    #     coords.append(canvas.coords(bots[i]))
            if side==2:
                if x2+20>800:
                    stoped=1
                    # canvas.delete(bots[i])
                    # bots[i] = canvas.create_rectangle(0, y1, 20, y2)
                else:
                    canvas.delete(energy[i])
                    energy_int[i] -= 1
                    canvas.move(bots[i], 20, 0)
                    # if energy_int[i]==0:
                    #     canvas.delete(bots[i])
                    #     bots = bots[:i] + bots[i + 1:]
                    #     energy = energy[:i] + energy[i + 1:]
                    #     energy_int = energy_int[:i] + energy_int[i + 1:]
                    #     coords = coords[:i] + coords[i + 1:]
                    # else:
                    #     energy[i] = canvas.create_text(canvas.coords(bots[i])[0]+10, canvas.coords(bots[i])[1]+10, text=str(energy_int[i]), fill='white')
                    #
                    #     coords.append(canvas.coords(bots[i]))
            if side==3:
                if y2+20>600:
                    stoped=1
                    # canvas.delete(bots[i])
                    # bots[i] = canvas.create_rectangle(x1, 20, x2, 0)
                else:
                    canvas.delete(energy[i])
                    energy_int[i] -= 1
                    canvas.move(bots[i], 0, 20 )
                    # if energy_int[i]==0:
                    #     canvas.delete(bots[i])
                    #     bots = bots[:i] + bots[i + 1:]
                    #     energy = energy[:i] + energy[i + 1:]
                    #     energy_int = energy_int[:i] + energy_int[i + 1:]
                    #     coords = coords[:i] + coords[i + 1:]
                    # else:
                    #     energy[i] = canvas.create_text(canvas.coords(bots[i])[0]+10, canvas.coords(bots[i])[1]+10, text=str(energy_int[i]), fill='white')
                    #
                    #     coords.append(canvas.coords(bots[i]))
            if side==4:
                if x1-20<0:
                    stoped=1
                    # canvas.delete(bots[i])
                    # bots[i] = canvas.create_rectangle(0, y1, 20, y2)
                else:
                    canvas.delete(energy[i])
                    energy_int[i] -= 1
                    canvas.move(bots[i], -20, 0 )


            if energy_int[i]==0:
                canvas.delete(bots[i])
                bots = bots[:i] + bots[i + 1:]
                energy = energy[:i] + energy[i + 1:]
                energy_int = energy_int[:i] + energy_int[i + 1:]
                coords = coords[:i] + coords[i + 1:]
            elif stoped!=1:
                energy[i] = canvas.create_text(canvas.coords(bots[i])[0]+10, canvas.coords(bots[i])[1]+10, text=str(energy_int[i]), fill='white')

                coords.append(canvas.coords(bots[i]))
                if canvas.coords(bots[i]) in food_coords:
                    for j in range(len(food)):
                        if canvas.coords(bots[i])==canvas.coords(food[j]):
                            canvas.delete(food[j])
                            food= food[:i] +food[i + 1:]
                            food_coords = food_coords[:i] +food_coords[i + 1:]
                            canvas.delete(energy[i])
                            energy_int[i] += 10
                            energy[i] = canvas.create_text(canvas.coords(bots[i])[0]+10, canvas.coords(bots[i])[1]+10, text=str(energy_int[i]), fill='white')

                            break
                if canvas.coords(bots[i]) in die_coords:
                    for j in range(len(die)):
                        if canvas.coords(bots[i])==canvas.coords(die[j]):
                            canvas.delete(die[j])
                            die= die[:i] +die[i + 1:]
                            die_coords = die_coords[:i] +die_coords[i + 1:]
                            canvas.delete(energy[i])
                            energy_int[i] -= 5
                            energy[i] = canvas.create_text(canvas.coords(bots[i])[0]+10, canvas.coords(bots[i])[1]+10, text=str(energy_int[i]), fill='white')

                            break
            stoped=0
            canvas.pack(fill=BOTH)
            i += 1

    # for i in range(len(food)):
    #     canvas.delete(food[i])
    if len(food)<=4:
        for t in range(10):
            x = randint(0, 40) * 20
            y = randint(0, 30) * 20
            if [x, y, x + 20, y + 20] not in coords:
                food.append(canvas.create_rectangle(x, y, x + 20, y + 20, fill='green'))
                food_coords.append(canvas.coords(food[t]))
    if len(die)<=4:
        print('Len ' +str(len(die)))
        for t in range(10):
            x = randint(0, 40) * 20
            y = randint(0, 30) * 20
            if [x, y, x + 20, y + 20] not in coords:
                die.append(canvas.create_rectangle(x, y, x + 20, y + 20, fill='red'))
                print('dewrfewf0' + str(len(die)))
                die_coords.append(canvas.coords(die[t]))

window=Tk()

window.geometry("800x600")

canvas = Canvas(window, width=800, height=600)
bots=[]
coords=[]
food=[]
food_coords=[]
energy=[]
energy_int=[]
die=[]
die_coords=[]
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
