# Dont Press the Button

import tkinter # Python GUI

window = tkinter.Tk() # Opens a window named...Tk
button = tkinter.Button(window, text="Do Not Press the Button!!", width=40) #Place message on button in window (Tk) with button width of 40 pixels
button.pack(padx=10, pady=10) # padding around the button

clickcount = 0 # variable to keep track how many times button clicked

def onClick(event): # Click loop
    global clickcount
    clickcount = clickcount + 1
    if clickcount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.") # updates note in button
    elif clickcount == 2:
        button.configure(text="Gah! Next time, no more button!")
    else:
        button.pack_forget() # Removes button

button.bind("<ButtonRelease-1>", onClick)

window.mainloop()
