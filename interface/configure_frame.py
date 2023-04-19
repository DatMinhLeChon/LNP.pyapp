from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from interface.public_val import *
from functools import partial

#configuration 
values = {"Maximize" : 1, "Minimize" : 0}


class ConfigureFrame(Frame):
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def applyConfigureData(self, spin_constraints, spin_variables):
        global public_number_const
        global public_number_val
        global signal_loop
        try:
            public_number_const = spin_constraints.get()
            public_number_val = spin_variables.get()
            signal_loop = 0
            self.parent.destroy()
        except:
            return IndexError
        
    def initUI(self):
        global objective_type
        
        self.parent.title("Dataset Configuration")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill = X, padx = 20, pady =20)
        
        frame2 = Frame(self)
        frame2.pack(fill= X, padx =20, pady =20)\
            
        frame3 = Frame(self)
        frame3.pack(fill = BOTH, expand = True)
        
        #configure number constrain 
        label_constraint = Label(frame1, text = "Number of Constraints")
        label_constraint.grid(column =1, row = 0, sticky= 'w')
        
        spin_constraint = Spinbox(frame1, from_= 2, to = 20)
        spin_constraint.grid(column = 2, row = 0, sticky ='e')
        
        
        #configure number variable
        label_variable = Label(frame1, text = "Number of Variables")
        label_variable.grid(column =1, row = 1, sticky ='w')
        
        spin_variable = Spinbox(frame1, from_= 2, to = 20)
        spin_variable.grid(column = 2, row = 1, sticky = 'e')
        
        #type of linear objective function
        label_frame = LabelFrame(frame2, text = "Objective")
        label_frame.pack(fill =X,anchor='sw' )
        
        for (text, value) in values.items():
            Radiobutton(label_frame, value = value, variable = objective_type, text = text).pack(side = TOP)

        Button2 = Button(frame3, text="OK", width =10, command = partial(self.applyConfigureData, spin_constraint, spin_variable))
        Button2.pack(side = RIGHT, padx=20, pady =5)
        

if __name__ =="__main__":
    root = Tk()
    root.geometry('300x350+200+200') 
    app= ConfigureFrame(root)
    root.mainloop()
# python interface\configure_frame.py