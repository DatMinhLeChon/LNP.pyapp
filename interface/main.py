from functools import partial
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from interface.main_frame import MainFrame
from interface.dataset_frame import DatasetFrame
from interface.configure_frame import ConfigureFrame
import sys

#def trigger(sheet_temp):
    #for i in range(sheet_temp.get_total_rows()):
        #if compare_string(sheet_temp.get_cell_data(i, 3, return_copy = True), \
        #sheet_temp.get_cell_data(i, 7,  return_copy = True), sheet_temp.get_cell_data(i, 4,  return_copy = True)) == 0:
            #sheet_temp.highlight_cells(row = i, column = 7, bg = "Red", fg = None, redraw = False, overwrite = True)
    # get_cell_data(r, c, return_copy = True)
    # highlight_cells(row = 0, column = 0, cells = [], canvas = "table", bg = None, fg = None, redraw = False, overwrite = True)

##_________button click in user interface main____thread & subprocess design 
def temp_click(txt): 
    txt.insert('1.0', "process successful ")


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
    app_temp = DatasetFrame(root_temp)
    root_temp.mainloop()
    
def viewModelTable(linear_programming, sheet):
            df = linear_programming.dataFrame()
            sheet.set_sheet_data(data = df.values.tolist(),\
                reset_col_positions = True,\
                reset_row_positions = True,\
                redraw = True,\
                verify = False,\
                reset_highlights = False)

def datasetApply(method_name, lhs_ineq, rhs_ineq, bnd):
    linear_programming = scipy_script.Model(method_name, lhs_ineq, rhs_ineq, bnd)
    return linear_programming

##Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

if __name__ == "__main__" :
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= MainFrame(root)
    root.mainloop()

#  python interface\main.py