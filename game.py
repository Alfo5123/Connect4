## GUI Toolkit
from Tkinter import *
import tkFont 

class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        police = tkFont.Font(family="Helvetica",size=36,weight="bold") 
        self.t = Label(self, text="Connect4 AI", font=police)
        self.t.grid(sticky=NSEW, pady=20)

class Point(object):

    def __init__(self, x, y, canvas, color="white"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.turn = 1
        self.r = 30
        self.point = self.canvas.create_oval(self.x+10,self.y+10,self.x+61,self.y+61,fill=color,outline="blue")

    def changeColor(self, color):
        self.canvas.itemconfigure(self.point, fill=color)
        self.color = color

class Terrain(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.turn = 1
        self.color = "yellow"
        self.p = []
        self.perm = True
        
        for i in range(0, 340, int(400/6)):
            liste_rangee = []
            for j in range(0, 440, int(500/7)):
                liste_rangee.append(Point(j, i ,self))
                
            self.p.append(liste_rangee)
        
        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x/71)
            lig = 0
            
            lig = 0
            while lig < len(self.p):            
                if self.p[0][col].color == "red" or self.p[0][0].color == "yellow":
                    break
                
                if self.p[lig][col].color == "red" or self.p[lig][col].color == "yellow":
                    self.p[lig-1][col].changeColor(self.color)
                    break
                
                elif lig == len(self.p)-1:
                    self.p[lig][col].changeColor(self.color)
                    break

                
                if self.p[lig][col].color != "red" and self.p[lig][col].color != "yellow":
                    lig+=1

            
            if self.turn == 1:
                self.turn = 2
                info.t.config(text="Computer's Turn")
                self.color = "red"

            elif self.turn == 2:
                self.turn = 1
                info.t.config(text="Your turn")
                self.color = "yellow"

            self.Horizontal()
            self.Vertical()
            self.Diagonal1()
            self.Diagonal2()

    def Horizontal(self):
        i = 0
        while(i < len(self.p)):
            j = 0
            while(j < 4):
                if(self.p[i][j].color == self.p[i][j+1].color == self.p[i][j+2].color == self.p[i][j+3].color == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].color == self.p[i][j+1].color == self.p[i][j+2].color == self.p[i][j+3].color == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j +=1
            i += 1

    def Vertical(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < len(self.p[i])):
                if(self.p[i][j].color == self.p[i+1][j].color == self.p[i+2][j].color == self.p[i+3][j].color == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].color == self.p[i+1][j].color == self.p[i+2][j].color == self.p[i+3][j].color == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j+=1
            i+=1

    def Diagonal1(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                if(self.p[i][j].color == self.p[i+1][j+1].color == self.p[i+2][j+2].color == self.p[i+3][j+3].color == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].color == self.p[i+1][j+1].color == self.p[i+2][j+2].color == self.p[i+3][j+3].color == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j += 1
            i += 1
                    
    def Diagonal2(self):
        i = 0
        while(i < 3):
            j = len(self.p[i])-1
            while(j > len(self.p)-4):
                if(self.p[i][j].color == self.p[i+1][j-1].color == self.p[i+2][j-2].color == self.p[i+3][j-3].color == "red"):
                    info.t.config(text="Victoire de rouge !")
                    self.perm = False
                    break
                elif(self.p[i][j].color == self.p[i+1][j-1].color == self.p[i+2][j-2].color == self.p[i+3][j-3].color == "yellow"):
                    info.t.config(text="Victoire de Jaune !")
                    self.perm = False
                    break
                j -= 1
            i += 1



root = Tk()
root.geometry("500x550")
root.title("Connect 4 AI Bot")
root.minsize(500,550)
root.maxsize(500,550)

info = Info(root)
info.grid(row=0, column=0)


t = Terrain(root)
t.grid(row=1, column=0)

def rein():
    global info
    info.t.config(text="")
    
    info = Info(root)
    info.grid(row=0, column=0)

    t = Terrain(root)
    t.grid(row=1, column=0)

Button(root, text="Try again (?)", command=rein).grid(row=2, column=0, pady=30)

root.mainloop()
