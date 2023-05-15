from tkinter.ttk import *
from tkinter import *
from interface.configure_frame import ConfigureFrame
from interface.result_frame import ResultFrame
from apply_model import applyModelLNP
from functools import partial, update_wrapper
import public_var
import tksheet
import pandas as pd
import numpy.matlib
import time

# Main frame
class MainFrame(Frame): # main frame
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    # change type of called prototype to run function: wrappedPartial(function_name, function_var_1, ....)
    def wrappedPartial(self, func, *args, **kwargs):
        partial_func = partial(func, *args, **kwargs)
        update_wrapper(partial_func, func)
        return partial_func

    def eventGetResultToPublicModel(self, txt):
        txt.delete('1.0', END)
        public_var.model_linear_programming = applyModelLNP()
        txt.insert("1.0", public_var.model_linear_programming.visualize())
    
    # processing table data from main frame to public_var
    def applyFirstDataFunctionLNP(self, sheet, txt): # fill here.
        number_ineq, number_eq = 0, 0 # init count variable
        for index1 in range(0, int(public_var.public_number_const)+1):
            if sheet.get_cell_data(index1, int(public_var.public_number_val)+1) == "<=" or \
            sheet.get_cell_data(index1, int(public_var.public_number_val)+1) == ">=":
                number_ineq += 1
            elif sheet.get_cell_data(index1, int(public_var.public_number_val)+1) == "=":
                number_eq += 1
        public_var.public_lhs_eq = [[0 for i in range(int(public_var.public_number_val))] for j in range(number_eq)]
        public_var.public_lhs_ineq = [[0 for i in range(int(public_var.public_number_val))] for j in range(number_ineq)]
        public_var.public_rhs_eq = [0 for i in range(number_eq)]
        public_var.public_rhs_ineq = [0 for i in range(number_ineq)]
        public_var.public_obj = [0 for i in range(int(public_var.public_number_val))]
        number_ineq, number_eq = 0, 0 # reset count variable 
        for index1 in range(0, int(public_var.public_number_const)):
            if sheet.get_cell_data(index1+1, int(public_var.public_number_val)+1) == "<=":
                for index2 in range(0, int(public_var.public_number_val)):
                    public_var.public_lhs_ineq[number_ineq][index2] = int(sheet.get_cell_data(index1 +1, index2 +1))
                public_var.public_rhs_ineq[number_ineq] = int(sheet.get_cell_data(index1 +1, int(public_var.public_number_val)+2))
                number_ineq +=1
            elif sheet.get_cell_data(index1+1, int(public_var.public_number_val)+1) == ">=":
                for index2 in range(0, int(public_var.public_number_val)):
                    public_var.public_lhs_ineq[number_ineq][index2] = -int(sheet.get_cell_data(index1 +1, index2 +1))
                public_var.public_rhs_ineq[number_ineq] = -int(sheet.get_cell_data(index1 +1, int(public_var.public_number_val)+2))
                number_ineq += 1
            elif sheet.get_cell_data(index1+1, int(public_var.public_number_val)+1) == "=":
                for index2 in range(0, int(public_var.public_number_val)):
                    public_var.public_lhs_eq[number_ineq][index2] == int(sheet.get_cell_data(index1 +1, index2 +1))
                public_var.public_rhs_ineq[number_eq] = int(sheet.get_cell_data(index1 +1, int(public_var.public_number_val)+2))
                number_eq += 1
        for index in range(0, int(public_var.public_number_val)):
            public_var.public_obj[index] = int(sheet.get_cell_data(0, int(public_var.public_number_val)))
        self.eventGetResultToPublicModel(txt)
        
    # create table at mainframe from last data from configure frame
    def eventViewModelTable(self, sheet, txt):
        temp_list = []
        temp_list.append('RN')
        for index in range(1, int(public_var.public_number_val)+1):
            temp_list.append(''.join(['x',str(index)]))
        temp_list.append('Sign')
        temp_list.append('Right side')
        # init a table objective ans constraints 
        try:
            df = pd.DataFrame(numpy.matlib.empty((int(public_var.public_number_const)+1,\
                int(public_var.public_number_val)+3)), columns = temp_list)
            sheet.set_sheet_data(data = df.values.tolist(),\
                        reset_col_positions = True,\
                        reset_row_positions = True,\
                        redraw = True,\
                        verify = False,\
                        reset_highlights = False,\
                        )
        except: pass
        # change table index 
        try:
            sheet.headers(temp_list)
            for index1 in range(0, int(public_var.public_number_const)+1):
                for index2 in range(0, int(public_var.public_number_val)+3):
                    if index2 == 0:
                        if index1 == 0:
                            sheet.set_cell_data(index1, index2, value = 'Objective', set_copy = True, redraw = False)
                        else:
                            sheet.set_cell_data(index1, index2, value = ''.join(['Constraint', str(index1)]), set_copy = True, redraw = False)
                    elif index2 == int(public_var.public_number_val)+1:
                        if index1 == 0:
                            sheet.set_cell_data(index1, index2, value = '||', set_copy = True, redraw = False)
                        else:
                            sheet.set_cell_data(index1, index2, value = '<=', set_copy = True, redraw = False)
                    elif (index1 == 0) and (index2 == int(public_var.public_number_val)+2):
                        if int(public_var.objective_type) == 1:
                            sheet.set_cell_data(index1, index2, value = 'Max', set_copy = True, redraw = False)
                        elif int(public_var.objective_type) == 0:
                            sheet.set_cell_data(index1, index2, value = 'Min', set_copy = True, redraw = False)
                        else:
                            sheet.set_cell_data(index1, index2, value = 'Unidentify', set_copy = True, redraw = False)
                    else:
                        sheet.set_cell_data(index1, index2, value = 0 , set_copy = True, redraw = False)
        except: pass
        try:
            txt.delete('1.0', END)
            txt.insert('1.0', "Entry data to this table!")
        except: pass
    
    # configure Frame checking ruuning
    # if nonrunning, the main frame create table with dataset from the last configure frame data return.
    def eventStartLoop(self, sheet, txt):
        if public_var.signal_loop == 1:
            self.parent.after(3000, self.wrappedPartial(self.eventStartLoop, sheet, txt))
        else:
            self.eventViewModelTable(sheet, txt)
    
    # function open configure frame, by event click button in mainframe
    def eventConfigurationFrameOpen(self, sheet, txt):
        public_var.signal_loop = 1
        root_temp= Toplevel()
        root_temp.geometry("300x350+300+300")
        app_temp = ConfigureFrame(root_temp)
        self.eventStartLoop(sheet, txt)
        root_temp.mainloop()
    
    # run result frame, and create model data from table data in the last fill at mainframe_table
    # applyFunctionLNP: function processing table data from mainframe
    def eventRunFunction(self, sheet, txt):
        root_temp = Toplevel()
        root_temp.geometry('300x350+300+300')
        public_var.result_lnp = self.applyFirstDataFunctionLNP(sheet,txt)
        app_temp =ResultFrame(root_temp)
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
        
        # button open configure Frame
        Button1_tab1 = Button(frame_main1, text="Linear Programming", width =1000, command= partial(self.eventConfigurationFrameOpen, sheet1, txt) )
        Button1_tab1.pack(side=LEFT, padx=5, pady=5)
        
        Button1_frame0 = Button(frame_main0, text="File", width =5, highlightthickness=0, relief="flat")
        Button1_frame0.pack(side=LEFT, padx=5, pady=5)
        Button2_frame0 = Button(frame_main0, text="Edit", width =5, highlightthickness=0, relief="flat")
        Button2_frame0.pack(side=LEFT, padx=5, pady=5)
        Button3_frame0 = Button(frame_main0, text="RUN", width =5, highlightthickness=0, relief="flat", command = partial(self.eventRunFunction, sheet1, txt))
        Button3_frame0.pack(side=LEFT, padx=5, pady=5)
        Button4_frame0 = Button(frame_main0, text="Help", width =5, highlightthickness=0, relief="flat")
        Button4_frame0.pack(side=LEFT, padx=5, pady=5)
        
if __name__ =="__main__":
    root = Tk()
    root.geometry('1200x600+200+200') 
    app= MainFrame(root)
    root.mainloop()

# python interface\main_frame.py ..