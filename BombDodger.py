# Bomb Dodger just like minesweep

# Set a stage.
# indicate where closest bomb is and how many.
# game ends when hit bomb or clear the board


import tkinter
import random

from tkinter.ttk import *

gameOver = False
score = 0
squareToClear = 0

def play_bombDodger():
    create_bombField(bombField)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()

bombField = []
def create_bombField(bombField):
    global squareToClear
    for row in range(0,10):
        rowList = []
        for column in range(0,10):
            if random.randint(1,100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squareToClear = squareToClear + 1
        bombField.append(rowList)
    #printfield(bombField)

def printfield(bombField):
    for rowList in bombField:
        print(rowList)

def layout_window(window):
    for rowNumber, rowList in enumerate(bombField): # enumerate is a function that goes through each item and index
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text = "    ", bg = "darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text = "    ", bg = "seagreen")
            else:
                square = tkinter.Label(window, text = "    ", bg = "green")
            square.grid(row = rowNumber, column = columnNumber)
            square.bind("<Button-1>", on_click)

def on_click(event):
    global score
    global gameOver
    global squareToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if bombField[row][column] == 1:
            gameOver = True
            square.config(bg = "red")
            print("Game Over! You hit a bomb!")
            print("Your score was", score)
        elif currentText == "    ":
            square.config(bg = "brown")
            totalBombs = 0
            if row < 9:
                if bombField[row+1][column] == 1:
                    totalBombs = totalBombs +1
            if row > 0:
                if bombField[row-1][column] == 1:
                    totalBombs = totalBombs +1
            if column > 0:
                if bombField[row][column-1] == 1:
                    totalBombs = totalBombs +1
            if column < 9:
                if bombField[row][column+1] == 1:
                    totalBombs = totalBombs +1
            if row > 0 and column > 0:
                if bombField[row-1][column-1] == 1:
                    totalBombs = totalBombs +1
            if row < 9 and column > 0:
                if bombField[row+1][column-1] == 1:
                    totalBombs = totalBombs +1
            if row > 0 and column < 9:
                if bombField[row-1][column+1] == 1:
                    totalBombs = totalBombs +1
            if row < 9 and column < 9:
                if bombField[row+1][column+1] == 1:
                    totalBombs = totalBombs +1
            square.config(text = " " + str(totalBombs) + " ")
            squareToClear = squareToClear - 1
            score = score +1
            if squareToClear == 0:
                gameOver = True
                print("Well done! You have found all the safe squares!")
                print("Your total score was:", score)

play_bombDodger()

