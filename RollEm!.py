#Written 29/8/22
#Dice roller! for TTRPGs

#importing the modules this script will need for the dice.
import random, math 
#importing the GUI function
import tkinter as tk
from tkinter import filedialog, Text
import os

#var for quantity of dice rolled
dQuantity = 0
#var for how many sides the dice have. 
dSides = 0

#defining each of the dice options
def dx():
  d4 = [d4i for d4i in range(4)]
  d6 = [d6i for d6i in range(6)]
  d8 = [d8i for d8i in range(8)]
  d10 = [d10i for d10i in range(10)]
  d12 = [d12i for d12i in range(12)]
  d20 = [d20i for d20i in range(20)]
  
#this establishes that I will be using a GUI
root = tk.Tk()
#establishes the title for our GUI
root.title('RollEm! a TTRPG Dice Roller')
#setting up how the canvas should be displayed
canvas = tk.Canvas(root, height=700, width=700, bg="Black")
#pack just says to put it onto the screen
canvas.pack()

#creates the space in the middle to be framed
frame = tk.Frame(root, bg="Green")
#determines the settings of the space that's being framed
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

ButtonRoll = tk.Button(root, text="Roll 'em!", padx=10, pady=10, fg="white", bg="black")
#attaches button to the canvas
ButtonRoll.pack()

#displays the GUI
root.mainloop()



#print("Hey Bozo! How many dice do you want to roll?")
#dQuantity = input()

#for idx, num in enumerate(dQuantity):
   # print(random.randint(1,10))
 #  print("it worked!")
#print(dQuantity)

