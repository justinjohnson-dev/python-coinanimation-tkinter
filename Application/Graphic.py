from tkinter import *
import time
import sys

window = Tk()
window.title("Person flipping a coin!")
canvas = Canvas(window, width=600, height=800)
canvas.pack()

head = canvas.create_oval(175,450,225,500,fill = "#e8d8c3")

body = canvas.create_rectangle(197,500,202,620, fill = "black")

rightBicept = canvas.create_line(200,540,250,540)

rightTricept = canvas.create_line(250,540,250,485)

rightHand = canvas.create_rectangle(240,475,260,485, fill = "#e8d8c3")

leftArm = canvas.create_line(200,540,150,540)

leftTricept = canvas.create_line(150,540,110,490)

leftLeg = canvas.create_line(197,620,140,690)

rightLeg = canvas.create_line(202,620,250,690)

def createCoin() :
    coin = (canvas.create_oval(240,455,260,475, fill = "gold"))
    return coin

def toss(x):
    window.lift()
    coin = createCoin()
    for y in range(x) :
          
        for i in range (60) :
            canvas.move(coin,0,-1)
            window.update()
            time.sleep(.01)
        
        for i in range (60) :
            canvas.move(coin, 0, 1)
            window.update()
            time.sleep(.01)
    canvas.delete(coin)

def close() :
    window.destroy()
        

