#!/usr/bin/env python

# Alfredo de la Fuente 2017

## GUI Toolkit
from Tkinter import *
import tkFont 
import random

## GUI Configuration

class Info(Frame):
	## Message in the top of screen
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100, bg="white")
        police = tkFont.Font(family="Arial",size=36,weight="bold") 
        self.t = Label(self, text="Connect4 AI", font=police, bg ="white")
        self.t.grid(sticky=NSEW, pady=20)

class Point(object):
	## Each one of the circles in the board
    def __init__(self, x, y, canvas, color="white"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.turn = 1
        self.r = 30
        self.point = self.canvas.create_oval(self.x+10,self.y+10,self.x+61,self.y+61,fill=color,outline="blue")

    def setColor(self, color):
        self.canvas.itemconfigure(self.point, fill=color)
        self.color = color


class Board(object):
	## Game basic dynamics
    def __init__(self, board ):
    	self.board = board 

    def tryMove(self, move):
    	# Takes the current board and a possible move specified 
    	# by the column. Returns the appropiate row where the 
    	# piece and be located. If it's not found it returns -1.

    	if ( move < 0 or move > 7 or self.board[0][move] != 0 ):
    		return -1 ;

    	for i in range(len(self.board)):
    		if ( self.board[i][move] != 0 ):
    			return i-1
    	return len(self.board)-1

    def terminal(self):
       # Returns true when the game is finished
        empty = 0 
        for i in range(len(self.board)):
       	  for j in range(len(self.board[0])):
       		if ( self.board[i][j] == 0 ):
       			empty = empty + 1 
        return empty==0

    def legal_moves(self):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        legal = []
        for i in range(len(self.board[0])):
        	if( self.board[0][i] == 0 ):
        		legal.append(i)

        return legal

    def winner(self):
        # Takes the board as input and determines if there is a winner.
        # If the game is now won, return the player number (Computer = 1, Human = -1).
        # If the game is still ongoing, return zero.  
	    i = 0
	    while(i < len(self.board)):
	        j = 0
	        while(j < 4):
	            if(self.board[i][j]== self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] == 1):
	                return 1
	            elif(self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] == -1):
	                return -1
	            j +=1
	        i += 1


	    i = 0
	    while(i < 3):
	        j = 0
	        while(j < len(self.board[i])):
	            if(self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] == 1):
	                return 1
	            elif(self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] == -1):
	                return -1
	            j+=1
	        i+=1


	    i = 0
	    while(i < 3):
	        j = 0
	        while(j < 3):
	            if(self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] == 1):
	                return 1
	            elif(self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] == -1):
	                return -1
	            j += 1
	        i += 1
	                    
	    i = 0
	    while(i < 3):
	        j = len(self.board[i])-1
	        while(j > len(self.board)-4):
	            if(self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] == 1):
	                return 1
	            elif(self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] == -1):
	                return -1
	            j -= 1
	        i += 1

	    return 0


class Terrain(Canvas):
	## Board visual representation
    def __init__(self, master=None):

        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.p = []
        self.winner = False

        board = [] 
        for i in range(6):
        	row = []
        	for j in range(7):
        		row.append(0)
        	board.append(row)

        self.b = Board( board )
        
        for i in range(0, 340, int(400/6)):
            spots = []
            for j in range(0, 440, int(500/7)):
                spots.append(Point(j, i ,self))
                
            self.p.append(spots)
        
        self.bind("<Button-1>", self.action)

    def action(self, event):

    	# Human Action
        if not self.winner:
            col = int(event.x/71)
            ok = False 
            row = self.b.tryMove( col )

            if row == -1:
            	return 
            else:
            	self.p[row][col].setColor("yellow")
                self.b.board[row][col] = -1
            	ok = True

            if ok:
	            info.t.config(text="Computer's Turn")

            result = self.b.winner()

            #Check if there is a winner or if it ended in a draw
            if result == 1:
            	info.t.config(text="You lost!")
            	self.winner = True 
            elif result == -1:
            	info.t.config(text="You won!")
            	self.winner = True
            elif self.b.terminal():
            	info.t.config(text="Draw")
            	self.winner = True 

        # Computer Action 	
        if not self.winner:

        	#Pick random move
        	moves = self.b.legal_moves()
        	ind = random.randint(0,len(moves)-1)
        	row = self.b.tryMove(moves[ind])

        	if row != -1: 
        		self.p[row][moves[ind]].setColor("red")
        		self.b.board[row][moves[ind]] = 1 
        		ok = True

        	if ok:
        		info.t.config(text="Your turn")

        	result = self.b.winner()

        	if result == 1 :
        		info.t.config(text="You lost!")
        		self.winner = True
        	elif result == -1:
        		info.t.config(text="You won!")
        		self.winner = 1
        	elif self.b.terminal():
        		info.t.config(text="Draw")
        		self.winner = True



if __name__ == "__main__":
	## Game execution
	root = Tk()
	root.geometry("500x550")
	root.title("Connect 4 AI Bot")
	root.configure(bg="white")
	root.minsize(500,600)
	root.maxsize(500,600)

	info = Info(root)
	info.grid(row=0, column=0)


	t = Terrain(root)
	t.grid(row=1, column=0)

	def restart():
	    global info
	    info.t.config(text="")
	    
	    info = Info(root)
	    info.grid(row=0, column=0)

	    t = Terrain(root)
	    t.grid(row=1, column=0)

	def close():
		root.destroy()

	Button(root, text="Try again (?)", command=restart).grid(row=2, column=0, pady=15)
	Button(root, text = "Exit", command = close).grid(row=3,column = 0, pady = 5)

	root.mainloop()
