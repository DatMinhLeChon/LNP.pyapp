from tkinter.ttk import *
from tkinter import *
from functools import partial
from public_var import *
import public_var
#configuration 

class ConfigureFrame(Frame):
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def applyObjectiveType(self, var):
        public_var.objective_type = var.get()

    def applyConfigureData(self, spin_constraints, spin_variables, var):
        public_var.signal_loop = 0
        try:
            public_var.public_number_const = spin_constraints.get()
            public_var.public_number_val = spin_variables.get()
            public_var.objective_type = var.get()
            self.parent.destroy()
        except:
            print('error')
        
    def initUI(self):
        self.parent.title("Dataset Configuration")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill = X, padx = 20, pady =20)
        frame2 = Frame(self)
        frame2.pack(fill= X, padx =20, pady =20)
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
        
        var_temp = IntVar()
        for (text, value) in public_var.values.items():
            Radiobutton(label_frame, value = value, variable = var_temp, command= self.applyObjectiveType(var_temp), text = text).pack(side = TOP)

        Button2 = Button(frame3, text="OK", width =10, command = partial(self.applyConfigureData, spin_constraint, spin_variable, var_temp))
        Button2.pack(side = RIGHT, padx=20, pady =5)
        

if __name__ =="__main__":
    root = Tk()
    root.geometry('300x350+200+200') 
    app= ConfigureFrame(root)
    root.mainloop()
# python interface\configure_frame.py›