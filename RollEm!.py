#Written 29/8/22
#Dice roller! for TTRPGs

#importing the modules this script will need for the dice.
import random, math 
#importing the GUI function
import tkinter as tk
from tkinter import *
import os

#var for quantity of dice rolled
dQuantity = 0
#var for how many sides the dice have. 
dSides = 0

#defining function for each of the dice options
def diceRanges(d4Q, d6Q, d8Q, d10Q, d12Q, d20Q):

    d4 = []
    d6 = []
    d8 = []
    d10 = []
    d12 = []
    d20 = []
#error checking these
    for i in range(1, int(d4Q)+1):
        d4.append(random.randint(1,4))
    for i in range(1, int(d6Q)+1):
        d6.append(random.randint(1,6))
    for i in range(1, int(d8Q)+1):
        d8.append(random.randint(1,8))
    for i in range(1, int(d10Q)+1):
        d10.append(random.randint(1,10))
    for i in range(1, int(d12Q)+1):
        d12.append(random.randint(1,12))
    for i in range(1, int(d20Q)+1):
        d20.append(random.randint(1,20))
    return d4, d6, d8, d10, d12, d20    

#defining function to Get the text inputs from the gui and assigning them into variables?
def rollEm():
    d4Q = d4Input.get()
    d6Q = d6Input.get()
    d8Q = d8Input.get()
    d10Q = d10Input.get()
    d12Q = d12Input.get()
    d20Q = d20Input.get()
  
    d4, d6, d8, d10, d12, d20 = diceRanges(d4Q, d6Q, d8Q, d10Q, d12Q, d20Q)

    print(d4, d6, d8, d10, d12, d20)

  

#this establishes that I will be using a GUI
root = tk.Tk()
#establishes the title for our GUI
root.title('RollEm! a TTRPG Dice Roller')
#setting up how the canvas should be displayed
root.geometry("420x420")  # set starting size of window

    
d4Input = Entry(root)
d6Input = Entry(root)
d8Input = Entry(root)
d10Input = Entry(root)
d12Input = Entry(root)
d20Input = Entry(root)

# grid method to arrange labels in respective
# rows and columns as specified


d4Text = Label(root, text = "How many d4 would you like to roll?", font='Calibri 10')
d4Text.grid(row = 1, column = 0, sticky = W, pady = 2)
#d4Input.grid(row = 1, column = 1, pady = 2)
d4Input.grid(row = 2, column = 0)

#gui d4 output
#d4Output = diceRanges(d4)
d4OutputText = Label(root, text = d4Input)
#d4OutputText.grid(row = 2, column = 0, pady = 2)
d4OutputText.grid(row = 1, column = 1, pady = 2)

d6Text = Label(root, text = "How many d6 would you like to roll?", font='Calibri 10')
d6Text.grid(row = 3, column = 0, pady = 2)
d6Input.grid(row = 4, column = 0)
#
d6OutputText = Label(root, text = "bazinga")
d6OutputText.grid(row = 3, column = 1, pady = 2)

d8Text = Label(root, text = "How many d8 would you like to roll?", font='Calibri 10')
d8Text.grid(row = 5, column = 0, sticky = W, pady = 2)
d8Input.grid(row = 6, column = 0)
#
d8OutputText = Label(root, text = "bazinga")
d8OutputText.grid(row = 5, column = 1, pady = 2)

d10Text = Label(root, text = "How many d10 would you like to roll?", font='Calibri 10')
d10Text.grid(row = 7, column = 0, sticky = W, pady = 2)
d10Input.grid(row = 8, column = 0)
#
d10OutputText = Label(root, text = "bazinga")
d10OutputText.grid(row = 7, column = 1, pady = 2)

d12Text = Label(root, text = "How many d12 would you like to roll?", font='Calibri 10')
d12Text.grid(row = 9, column = 0, sticky = W, pady = 2)
d12Input.grid(row = 10, column = 0)
#
d12OutputText = Label(root, text = "bazinga")
d12OutputText.grid(row = 9, column = 1, pady = 2)

d20Text = Label(root, text = "How many d20 would you like to roll?", font='Calibri 10')
d20Text.grid(row = 11, column = 0, sticky = W, pady = 2)
d20Input.grid(row = 12, column = 0)
#
#d20OutputText = Label(root, text = rollEm(d4))
d20OutputText = Label(root, text = "bazinga")
d20OutputText.grid(row = 11, column = 1, pady = 2)

RollButton = Button(root, text= "Roll Em!", command=rollEm).grid()














#displays the GUI/End of the GUI section
root.mainloop()


#Old code that might be useful  ¯\_(ツ)_/¯
#print("Hey Bozo! How many dice do you want to roll?")
#dQuantity = input()

#for idx, num in enumerate(dQuantity):
   # print(random.randint(1,10))
 #  print("it worked! This concludes this test.")
#print(dQuantity)


#canvas = tk.Canvas(root, height=700, width=700, bg="Black")
#
#pack just says to put it onto the screen:
#canvas.pack()
#

#creates the space in the middle to be framed
#frame = tk.Frame(root, bg="Green")
#determines the settings of the space that's being framed
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#ButtonRoll = tk.Button(root, text="Roll 'em!", padx=10, pady=10, fg="white", bg="black", command= rollEm)
#attaches button to the canvas
#ButtonRoll.pack()

#This is where the d4 Label is created so you know what text box you are entering for
#d4TextBox = Label(frame, text='How many D4 would you like to roll?', font= ('Helvetica',12))
#This is where the d4 quantity input is created and inserted.
#d4Input = Entry(frame, width= 10, borderwidth= 5)
#d4Output = Label(frame, text= d4Op)
#d4TextBox.pack()
#d4Input.pack()

#This is where the d6 Label is created so you know what text box you are entering for
#d6TextBox = Label(frame, text='How many D6 would you like to roll?', font= ('Helvetica',12))
#This is where the d6 quantity input is created and inserted.
#d6Input = Entry(frame, width= 10, borderwidth= 5)
#d6Output = Label(frame, text= d6Op)
#d6TextBox.pack()
#d6Input.pack()

#This is where the d8 Label is created so you know what text box you are entering for
#d8TextBox = Label(frame, text='How many D8 would you like to roll?', font= ('Helvetica',12))
#This is where the d8 quantity input is created and inserted.
#d8Input = Entry(frame, width= 10, borderwidth= 5)
#d8Output = Label(frame, text= d8Op)
#d8TextBox.pack()
#d8Input.pack()

#This is where the d10 Label is created so you know what text box you are entering for
#d10TextBox = Label(frame, text='How many D10 would you like to roll?', font= ('Helvetica',12))
#This is where the d4 quantity input is created and inserted.
#d10Input = Entry(frame, width= 10, borderwidth= 5)
#d10Output = Label(frame, text= d10Op)
#d10TextBox.pack()
#d10Input.pack()

#This is where the d12 Label is created so you know what text box you are entering for
#d12TextBox = Label(frame, text='How many D12 would you like to roll?', font= ('Helvetica',12))
#This is where the d12 quantity input is created and inserted.
#d12Input = Entry(frame, width= 10, borderwidth= 5)
#d12Output = Label(frame, text= d12Op)
#d12TextBox.pack()
#d12Input.pack()

#This is where the d20 Label is created so you know what text box you are entering for
#d20TextBox = Label(frame, text='How many D20 would you like to roll?', font= ('Helvetica',12))
#This is where the D20 quantity input is created and inserted.
#d20Input = Entry(frame, width= 10, borderwidth= 5)
#d20Output = Label(frame, text= d20Op)
#d20TextBox.pack()
#d20Input.pack()


#Working towards outputting the desired rolls
#d4RollTextBox = Label(frame, d4Rolls)