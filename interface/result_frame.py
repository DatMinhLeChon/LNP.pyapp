from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

class ResultFrame(Frame):
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Data")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill = X)
        frame2 = Frame(self)
        frame2.pack(fill= X)
        frame3 = Frame(self)
        frame3.pack(fill = BOTH)
        
        text1 = Text(frame1, text= None, width = 10)
        text1.pack(fill = X, padx =5, pady =5)
        
        Button2 = Button(frame2, text="End", width =5)
        Button2.pack(side = RIGHT, padx=5, pady =5)