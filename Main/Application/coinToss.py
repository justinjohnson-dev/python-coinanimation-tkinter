import random as r
from tkinter import *
import time
import Graphic
import time

print("This program simulates the tossing of a coin. The program generates ""\n"
      "a random number in range 1 through 2. If the number is 1, the function ""\n"
      "should display heads. If the random number is 2, function should display tails.")

def coinToss():
    again = 'y'
    while again == 'y' :
        nTosses = int(input("\nHow many tosses should I make? "))
        Graphic.toss(nTosses)
        for x in range(nTosses) :
            lToss = r.randint(1,2)
            if lToss == 1 :
                print(x + 1,":","\tHeads",sep=(""))
            elif lToss == 2 :
                print(x + 1,":","\tTails",sep=(""))   
        again = input("\nWould you like to flip the coin again? (y = yes): ")
    Graphic.close()
      
coinToss()        

