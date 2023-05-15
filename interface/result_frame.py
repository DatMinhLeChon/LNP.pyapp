from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import public_var

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
        
        label1 = Label(frame1, text ="Optimize Value", width = 10, height = 2)
        label1.pack(side =LEFT, padx =5, pady =5)
        
        text1 = Text(frame1, width = 10, height = 2)
        text1.pack(fill = BOTH, padx =5, pady =5)
        text1.insert("1.0", str(public_var.model_linear_programming.visualize()))
        
        label2 = Label(frame2, text ="Variable Values", width = 10, height = 2)
        label2.pack(side =LEFT, padx =5, pady =5)
        
        text2 = Text(frame2, width = 10, height = 2)
        text2.pack(fill = BOTH, padx =5, pady =5)
        text2.insert("1.0", str(public_var.model_linear_programming.linearProgramming().x))
        
        Button2 = Button(frame3, text="End", width =5)
        Button2.pack(side = BOTTOM, padx=5, pady =5)
        

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x300+200+200")
    app =ResultFrame(root)
    root.mainloop()

## python3 interface/result_frame.py