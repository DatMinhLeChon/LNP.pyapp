from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import tksheet

#configuration 

class ConfigureFrame(Frame):
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Dataset Configuration")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill = X, padx = 20, pady =20)
        frame2 = Frame(self)
        frame2.pack(fill= X)
        frame3 = Frame(self)
        frame3.pack(fill = BOTH)
        
        #configure number constrain 
        panel_number_const = Frame(frame1)
        panel_number_const.grid( row = 0)
        
        label_constraint = Label(panel_number_const, text = "Number of Constraints")
        label_constraint.grid(column =1, row =0, sticky= 'w')
        
        spin_constraint = Spinbox(panel_number_const, from_= 2, to = 20)
        spin_constraint.grid(column = 2, row = 0, sticky ='e')
        
        
        #configure number variable
        panel_number_val = Frame(frame1)
        panel_number_val.grid( row =1)
        
        label_variable = Label(panel_number_val, text = "Number of Variables")
        label_variable.grid(column =1, row =0, sticky ='w')
        
        spin_constraint = Spinbox(panel_number_val, from_= 2, to = 20)
        spin_constraint.grid(column = 2, row = 0, sticky = 'e')
        
        #type of linear objective function
        
        panel_objective = PanedWindow()
        
        Button1 = Button(frame1, text ="Run", width =15)
        
        Button2 = Button(frame2, text="End", width =5)
        Button2.pack(side = RIGHT, padx=5, pady =5)
        
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('600x400+200+200') 
    app= ConfigureFrame(root)
    root.mainloop()
# python interface\configure_frame.py