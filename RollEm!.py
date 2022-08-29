#Written 29/8/22
#Dice roller! for TTRPGs

#importing the modules this script will need for the dice.
import random, math 
#importing the GUI function
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
#setting up how the canvas should be displayed
canvas = tk.Canvas(root, height=700, width=700, bg="Purple")
#
canvas.pack()

#creates the space in the middle to be framed
frame = tk.Frame(root, bg="Gold")
#determines the settings of the space that's being framed
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

ButtonRoll = tk.Button(root, text="Roll 'em!", padx=10, pady=10, fg="white", bg="black")
#attaches button to the canvas
ButtonRoll.pack()
root.mainloop()

#var for quantity of dice rolled
#dQuantity = 0
#var for how many sides the dice have. 
#dSides = 0

#print("Hey Bozo! How many dice do you want to roll?")
#dQuantity = input()

#for idx, num in enumerate(dQuantity):
   # print(random.randint(1,10))
 #  print("it worked!")
#print(dQuantity)

