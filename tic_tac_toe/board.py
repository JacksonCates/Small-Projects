from tkinter import *
from math import floor

# This class does the tic-tac-toe board logic (checking for wins) and board drawing
class Board:

    # Constructor: creates empty board arrays and draws if indicated true
    def __init__(self, draw = True):
        # logic
        self.GotClick = False
        self.boardArray = [[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']]

        # Checks if it needs to draw
        if (draw):
            self.Draw()

    def Draw(self):
        
        # Draws the canvas
        self.root = Tk()
        self.root.title("Tic-tac-toe!")
        self.root.geometry('300x350')
        self.c = Canvas(self.root, height = 300, width = 300, bg = "white")
        
        # Creates the boarders
        self.c.create_line(100, 0, 100, 300)
        self.c.create_line(200, 0, 200, 300)
        self.c.create_line(0, 100, 300, 100)
        self.c.create_line(0, 200, 300, 200)

        # Binds clicking
        self.c.bind("<Button-1>", self.leftClick)

        self.c.pack()

    # This functions returns the canvas
    def GetCanvas(self):
        return self.c

    # This function updates the canvas for a click
    def Update(self):
        self.GotClick = False
        self.c.update()

    # This is an event that updates the variables x and y and GotClick
    def leftClick(self, event):
        x, y = event.x, event.y
        
        # Converts to coords
        self.x = floor(x / 100) * 100
        self.y = floor(y / 100) * 100

        # Updates
        self.GotClick = True

    # This function draws the X or O depending on who's turn it is
    def Mark(self, playerTurn):
        if playerTurn:
            # Creates the X
            self.c.create_line(self.x, self.y, self.x + 100, self.y + 100, width = 3)
            self.c.create_line(self.x + 100, self.y, self.x, self.y + 100, width = 3)
            self.SetCurrMark('x')
        else:
            self.c.create_oval(self.x, self.y, self.x + 100, self.y + 100, width = 3)
            self.SetCurrMark('o')

        # updates
        self.c.pack()

    # This function returns the current mark
    # The marks are ' ' for blank, 'x' for X, and 'o' for O
    def GetMark(self, x, y):
        return self.boardArray[x][y]

    # This returns the current mark stored (usually for clicking)
    def GetCurrMark(self):
        return self.boardArray[int(self.x/100)][int(self.y/100)]

    # This function sets the current mark to the new mark
    def SetCurrMark(self, newMark):
        self.boardArray[int(self.x/100)][int(self.y/100)] = newMark

    # This function selects a mark to be changed
    def SetMark(self, x, y, newMark):
        self.boardArray[x][y] = newMark

    # This function changes the current coordinates from clicking manually
    def SetCurrCoords(self, x, y):
        self.x = x * 100
        self.y = y * 100

    # This function prints the board array in console for debugging
    def PrintBoardArray(self):
        for y in range(0, 3):
            print('{} {} {}'.format(self.boardArray[0][y], self.boardArray[1][y], self.boardArray[2][y]))

    # Returns ' ' for no winner, 't' for tie, and the player's mark if they are the winner
    def DidPlayerWin(self, drawStrike = True):
        # Takes the original coordinate and checks around it
        for curr in range(0, 3):
            # Checks vertical
            if self.GetMark(curr, 0) == 'o' and self.GetMark(curr, 1) == 'o' and self.GetMark(curr, 2) == 'o':
                # Draws
                if drawStrike:
                    self.c.create_line(curr * 100 + 50, 0, curr * 100 + 50, 300, fill = 'red', width = 5)
                return 'o'
            if self.GetMark(curr, 0) == 'x' and self.GetMark(curr, 1) == 'x' and self.GetMark(curr, 2) == 'x':
                if drawStrike:
                    self.c.create_line(curr * 100 + 50, 0, curr * 100 + 50, 300, fill = 'red', width = 5)
                return 'x'

            # Checks horizontal
            if self.GetMark(0, curr) == 'o' and self.GetMark(1, curr) == 'o' and self.GetMark(2, curr) == 'o':
                if drawStrike:
                    self.c.create_line(0, curr * 100 + 50, 300, curr * 100 + 50, fill = 'red', width = 5)
                return 'o'
            if self.GetMark(0, curr) == 'x' and self.GetMark(1, curr) == 'x' and self.GetMark(2, curr) == 'x':
                if drawStrike:
                    self.c.create_line(0, curr * 100 + 50, 300, curr * 100 + 50, fill = 'red', width = 5)
                return 'x'
        
        # Checks diagonals
        if self.GetMark(0, 0) == 'o' and self.GetMark(1, 1) == 'o' and self.GetMark(2, 2) == 'o':
            if drawStrike:
                self.c.create_line(0, 0, 300, 300, fill = 'red', width = 5)
            return 'o'
        if self.GetMark(2, 0) == 'o' and self.GetMark(1, 1) == 'o' and self.GetMark(0, 2) == 'o':
            if drawStrike:
                self.c.create_line(300, 0, 0, 300, fill = 'red', width = 5)
            return 'o'
        if self.GetMark(0, 0) == 'x' and self.GetMark(1, 1) == 'x' and self.GetMark(2, 2) == 'x':
            if drawStrike:
                self.c.create_line(0, 0, 300, 300, fill = 'red', width = 5)
            return 'x'
        if self.GetMark(2, 0) == 'x' and self.GetMark(1, 1) == 'x' and self.GetMark(0, 2) == 'x':
            if drawStrike:
                self.c.create_line(300, 0, 0, 300, fill = 'red', width = 5)
            return 'x'

        # Finally we will check for a tie
        for x in range(0, 3):
            for y in range(0, 3):
                if self.GetMark(x, y) == ' ':
                    return  ' '

        # Else it is a tie
        return 't'