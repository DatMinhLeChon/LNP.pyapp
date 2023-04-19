from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from interface.configure_frame import ConfigureFrame
from interface.public_val import *
import tksheet
import pandas as pd
import numpy.matlib
import numpy as np

#def trigger(sheet_temp):
    #for i in range(sheet_temp.get_total_rows()):
        #if compare_string(sheet_temp.get_cell_data(i, 3, return_copy = True), \
        #sheet_temp.get_cell_data(i, 7,  return_copy = True), sheet_temp.get_cell_data(i, 4,  return_copy = True)) == 0:
            #sheet_temp.highlight_cells(row = i, column = 7, bg = "Red", fg = None, redraw = False, overwrite = True)
    # get_cell_data(r, c, return_copy = True)
    # highlight_cells(row = 0, column = 0, cells = [], canvas = "table", bg = None, fg = None, redraw = False, overwrite = True)

##_________button click in user interface main____thread & subprocess design 
    
def viewModelTable(sheet):
    global public_number_const
    global public_number_val
    temp_list = []
    temp_list.append('')
    for index in range(1, public_number_val+1):
        temp_list.append(''.join(['x',str(index)]))
    temp_list.append('Sign')
    temp_list.append('Right side')
    df = pd.DataFrame(np.matlib.empty((public_number_const, public_number_val+3)), columns = temp_list)
    sheet.set_sheet_data(data = df.values.tolist(),\
                reset_col_positions = True,\
                reset_row_positions = True,\
                redraw = True,\
                verify = False,\
                reset_highlights = False)

def configurationFrameOpen():
    global state_in_root_temp
    global signal_loop
    global root_temp
    signal_loop = 1
    root_temp= Tk()
    root_temp.geometry("300x350+300+300")
    app_temp = ConfigureFrame(root_temp)
    root_temp.mainloop()

class MainFrame(Frame): # main frame
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
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
        
        txt = Text(frame_main2, bg ="#fcfcfc", height= 2)
        txt.pack(fill=BOTH, pady=0, padx=5, expand=True)
    
        Button_tab1_4 = Button(frame_main1, text="Linear Programming", width =20, command= configurationFrameOpen )
        Button_tab1_4.pack(side=LEFT, padx=5, pady=5)
    
    
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= MainFrame(root)
    root.mainloop()

# python interface\main_frame.py