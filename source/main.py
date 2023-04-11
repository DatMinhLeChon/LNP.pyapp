from functools import partial
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import tksheet 
import threading
import ui_def
from val_def import Model

linear_programming = Model()

def clickRunRootTemp(): # env static val processing for auto loop
    global state_in_root_temp
    global signal_loop
    state_in_root_temp = 'run'
    signal_loop = 1
    messagebox.showinfo(title= "Message", message="Start auto")

def clickExitRootTemp(): # exit button fucnton in auto frame
    global state_in_root_temp
    global signal_loop
    state_in_root_temp = 'end'
    signal_loop = 0
    

def clickedFrameDataset(): # init auto frame by click button
    global state_in_root_temp
    global signal_loop
    signal_loop = 1
    root_temp= Tk()
    root_temp.geometry("400x80+300+300")
    app_temp = CheckingRunning(root_temp)
    root_temp.mainloop()
    
def viewModelTable(linear_programming, sheet):
            df = linear_programming.dataFrame()
            sheet.set_sheet_data(data = df.values.tolist(),\
                reset_col_positions = True,\
                reset_row_positions = True,\
                redraw = True,\
                verify = False,\
                reset_highlights = False)


def trigger(sheet_temp):
    for i in range(sheet_temp.get_total_rows()):
        if compare_string(sheet_temp.get_cell_data(i, 3, return_copy = True), \
        sheet_temp.get_cell_data(i, 7,  return_copy = True), sheet_temp.get_cell_data(i, 4,  return_copy = True)) == 0:
            sheet_temp.highlight_cells(row = i, column = 7, bg = "Red", fg = None, redraw = False, overwrite = True)
    # get_cell_data(r, c, return_copy = True)
    # highlight_cells(row = 0, column = 0, cells = [], canvas = "table", bg = None, fg = None, redraw = False, overwrite = True)

class Example(Frame): # main frame
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("LP Computing")
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
    
        Button_tab1_4 = Button(frame_main1, text="Linear Programming", width =10, )
        Button_tab1_4.pack(side=LEFT, padx=5, pady=5)
        
        

class CheckingRunning(Frame):
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
        
        sheet1 =tksheet.Sheet(frame3, data = [[]], height = 800, width = 1500)
        sheet1.pack(fill=BOTH, pady=10, padx=5, expand=True)
        sheet1.grid(row =20, column = 20,sticky="nswe")
        sheet1.enable_bindings()
        
        Button1 = Button(frame1, text ="Run",width =15, command= partial(viewModelTable, linear_programing, sheet1))
        Button1.pack(side = BOTTOM, padx =5, pady=5)
        
        Button2 = Button(frame2, text="End", width =5)
        Button2.pack(side = RIGHT, padx=5, pady =5)

if __name__ == "__main__" :
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= Example(root)
    root.mainloop()

# python3 source/main.py