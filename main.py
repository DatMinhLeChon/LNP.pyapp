from functools import partial
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from interface.main_frame import *
from module import *


##Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

if __name__ =="__main__":
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= MainFrame(root)
    root.mainloop()


#  python main.py