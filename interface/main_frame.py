from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from interface.configure_frame import ConfigureFrame
from interface.public_val import *
import interface.public_val
import tksheet
import pandas as pd
import numpy.matlib
import numpy as np
from functools import partial, update_wrapper

def wrapped_partial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func

""" Frame first """
class MainFrame(Frame): # main frame
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def viewModelTable(self, sheet):
        temp_list = []
        temp_list.append('RN')
        for index in range(1, int(interface.public_val.public_number_val)+1):
            temp_list.append(''.join(['x',str(index)]))
        temp_list.append('Sign')
        temp_list.append('Right side')
        print(temp_list)
        try:
            df = pd.DataFrame(numpy.matlib.empty((int(interface.public_val.public_number_const)+1,\
                int(interface.public_val.public_number_val)+3)), columns = temp_list)
            sheet.set_sheet_data(data = df.values.tolist(),\
                        reset_col_positions = True,\
                        reset_row_positions = True,\
                        redraw = True,\
                        verify = False,\
                        reset_highlights = False,\
                        )
        except:
            pass
        sheet.headers(temp_list)
        for index1 in range(0, int(interface.public_val.public_number_const)):
            for index2 in range(0, int(interface.public_val.public_number_val)+2):
                if index1 == 0:
                    if index2 == 0:
                        sheet.set_cell_data(index2, index1, value = 'Objective', set_copy = True, redraw = False)
                    else:
                        sheet.set_cell_data(index2, index1, value = ''.join(['Constraint', str(index2)]), set_copy = True, redraw = False)
                else:
                    if index1 == int(interface.public_val.public_number_val)+1:
                        sheet.set_cell_data(index2, index1, value = '<=', set_copy = True, redraw = False)
                    else:
                        sheet.set_cell_data(index2, index1, value = 0 , set_copy = True, redraw = False)
            
            
    def startLoop(self, sheet):
        if interface.public_val.signal_loop == 1:
            self.parent.after(3000, wrapped_partial(self.startLoop,sheet))
        else:
            self.viewModelTable(sheet)
            
    def configurationFrameOpen(self,sheet):
        interface.public_val.signal_loop = 1
        root_temp= Tk()
        root_temp.geometry("300x350+300+300")
        app_temp = ConfigureFrame(root_temp)
        self.startLoop(sheet)
        root_temp.mainloop()
        
    def initUI(self):
        self.parent.title("LNP Computing")
        self.pack(fill=BOTH, expand=True)
        
        # Main uI 
        frame_main1 = Frame(self)
        frame_main1.pack(fill=X)
        frame_main2 = Frame(self)
        frame_main2.pack(fill=X)
        frame_main3 = Frame(self)
        frame_main3.pack(side= LEFT, fill=Y, pady=5, padx =5)
        
        sheet1 =tksheet.Sheet(frame_main3, data = [[]], height = 800, width = 1500)
        sheet1.pack(fill=BOTH, pady=10, padx=5, expand=True)
        sheet1.grid(row =20, column = 20,sticky="nswe")
        sheet1.enable_bindings()
        
        txt = Text(frame_main1, bg ="#fcfcfc", height= 2)
        txt.pack(fill=BOTH, pady=0, padx=5, expand=True)
    
        Button_tab1_1 = Button(frame_main1, text="Linear Programming", width =20, command= partial(self.configurationFrameOpen, sheet1) )
        Button_tab1_1.pack(side=LEFT, padx=5, pady=5)
        Button_tab1_2 = Button(frame_main1, text="RUN", width =20)
        Button_tab1_2.pack(side=RIGHT, padx=5, pady=5)
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= MainFrame(root)
    root.mainloop()

# python interface\main_frame.py