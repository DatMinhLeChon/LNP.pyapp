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

def wrappedPartial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func

""" Main Frame """
class MainFrame(Frame): # main frame
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def viewModelTable(self, sheet, txt):
        temp_list = []
        temp_list.append('RN')
        for index in range(1, int(interface.public_val.public_number_val)+1):
            temp_list.append(''.join(['x',str(index)]))
        temp_list.append('Sign')
        temp_list.append('Right side')
        # init a table objective ans constraints 
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
        # change table index 
        try:
            sheet.headers(temp_list)
            for index1 in range(0, int(interface.public_val.public_number_const)+1):
                for index2 in range(0, int(interface.public_val.public_number_val)+3):
                    if index2 == 0:
                        if index1 == 0:
                            sheet.set_cell_data(index1, index2, value = 'Objective', set_copy = True, redraw = False)
                        else:
                            sheet.set_cell_data(index1, index2, value = ''.join(['Constraint', str(index1)]), set_copy = True, redraw = False)
                    elif index2 == int(interface.public_val.public_number_val)+1:
                        if index1 == 0:
                            sheet.set_cell_data(index1, index2, value = '||', set_copy = True, redraw = False)
                        else:
                            sheet.set_cell_data(index1, index2, value = '<=', set_copy = True, redraw = False)
                    elif (index1 == 0) and (index2 == int(interface.public_val.public_number_val)+2):
                        if interface.public_val.objective_type == 1:
                            sheet.set_cell_data(index1, index2, value = 'Max', set_copy = True, redraw = False)
                        elif interface.public_val.objective_type == 0:
                            sheet.set_cell_data(index1, index2, value = 'Min', set_copy = True, redraw = False)
                        else:
                            sheet.set_cell_data(index1, index2, value = 'Unidentify', set_copy = True, redraw = False)
                    else:
                        sheet.set_cell_data(index1, index2, value = 0 , set_copy = True, redraw = False)
                        
        except:
            pass
        try:
            txt.insert('1.0', "Entry data to this table!")
        except:
            pass
            
    def startLoop(self, sheet, txt):
        if interface.public_val.signal_loop == 1:
            self.parent.after(3000, wrappedPartial(self.startLoop, sheet, txt))
        else:
            self.viewModelTable(sheet, txt)
            
    def configurationFrameOpen(self, sheet, txt):
        interface.public_val.signal_loop = 1
        root_temp= Tk()
        root_temp.geometry("300x350+300+300")
        app_temp = ConfigureFrame(root_temp)
        self.startLoop(sheet, txt)
        root_temp.mainloop()
        
    def initUI(self):
        self.parent.title("LNP Computing")
        self.pack(fill=BOTH, expand=True)
        
        # Main uI 
        frame_main0 = Frame(self)
        frame_main0.pack(fill=X)
        frame_main1 = Frame(self)
        frame_main1.pack(fill=X)
        frame_main2 = Frame(self)
        frame_main2.pack(side= LEFT, fill=Y, pady=5, padx =5)
        frame_main3 = Frame(self)
        frame_main3.pack(side= LEFT, fill=Y, pady=5, padx =5)
        frame_main4 = Frame(self)
        frame_main4.pack(side= LEFT, fill=Y, pady=5, padx =5)
        
        sheet1 =tksheet.Sheet(frame_main3, data = [[]], height= 1000, width = 10000)
        sheet1.pack(fill=BOTH, pady=10, padx=5, expand=True)
        sheet1.grid(row =20, column = 20,sticky="nswe")
        sheet1.enable_bindings()
        
        txt = Text(frame_main2, bg ="#fcfcfc", height= 2, width = 20)
        txt.pack(fill=BOTH, pady=0, padx=5, expand=True)
    
        Button1_tab1 = Button(frame_main1, text="Linear Programming", width =1000, command= partial(self.configurationFrameOpen, sheet1, txt) )
        Button1_tab1.pack(side=LEFT, padx=5, pady=5)
        
        Button1_frame0 = Button(frame_main0, text="File", width =5, highlightthickness=0, relief="flat")
        Button1_frame0.pack(side=LEFT, padx=5, pady=5)
        Button2_frame0 = Button(frame_main0, text="Edit", width =5, highlightthickness=0, relief="flat")
        Button2_frame0.pack(side=LEFT, padx=5, pady=5)
        Button3_frame0 = Button(frame_main0, text="RUN", width =5, highlightthickness=0, relief="flat")
        Button3_frame0.pack(side=LEFT, padx=5, pady=5)
        Button4_frame0 = Button(frame_main0, text="Help", width =5, highlightthickness=0, relief="flat")
        Button4_frame0.pack(side=LEFT, padx=5, pady=5)
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= MainFrame(root)
    root.mainloop()

# python interface\main_frame.py