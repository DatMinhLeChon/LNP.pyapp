from tkinter.ttk import *
from tkinter import *
from interface.main_frame import *
from model import *
import public_var 


##Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

if __name__ =="__main__":
    public_var.root_main = Tk()
    public_var.root_main.geometry('1200x600+200+200') 
    public_var.root_main.config(bg="white")
    app = MainFrame(public_var.root_main)
    public_var.root_main.mainloop()


#  python main.py