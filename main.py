from functools import partial
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from interface.main_frame import *
from model import *
from interface.public_val import root_main


##Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

if __name__ =="__main__":
    root_main = Tk()
    root_main.geometry('1200x600+200+200') 
    app = MainFrame(root_main)
    root_main.mainloop()


#  python main.py