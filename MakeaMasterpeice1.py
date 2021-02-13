# Make a Masterpeice

import tkinter

print("To draw, hold down the left mous button and move your mouse around.")
print("To change your brush colour, click on one of the colours.")

def storePosition(event): # tracking mouse location as it moves
    global lastX, lastY
    lastX = event.x
    lastY = event.y
    
def onClick(event): 
    storePosition(event) # storing location when canvas clicked
    
def onDrag(event): # tracking when drawing to storePosition
    canvas.create_line(lastX, lastY, event.x, event.y, fill = colour, width = 3)
    storePosition(event)

def setColourRed(event):
    global colour
    colour="red"
def setColourBlue(event):
    global colour
    colour="blue"
def setColourBlack(event):
    global colour
    colour="black"
def setColourwhite(event):
    global colour
    colour="white"

window = tkinter.Tk() # creating the window
canvas = tkinter.Canvas(window, width=750, height=500, bg="white") # defining the window size and base colour
canvas.pack() # unlike Turtle and windows in general 'Canvas' the 0 x and y axis start in top left corner instead of centre.

lastX, lastY = 0,0
colour = "black"

# creating colours squares to select paint options, numbers are the location of boxes these are ID's on canvas
red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = canvas.create_rectangle(10, 85, 30, 105, fill="white") # Functions to change colour when called.
canvas.tag_bind(red_id, "<Button-1>", setColourRed)
canvas.tag_bind(blue_id, "<Button-1>", setColourBlue)
canvas.tag_bind(black_id, "<Button-1>", setColourBlack)
canvas.tag_bind(white_id, "<Button-1>", setColourwhite)
# binding the colour when mous clicked on corrosponding box

canvas.bind("<Button-1>", onClick) # Binds left mouse click
canvas.bind("<B1-Motion>", onDrag) # Binds the Motion when left mouse is clicked and held
window.mainloop()

