import subprocess
import threading
from tkinter import messagebox
from apscheduler.schedulers.blocking import BlockingScheduler

state_in_root_temp = 'end'


## Home button click to run function 10 time of runnning 2 main file, and draw plot to compare runtime

## Function for button auto run in tab LASER P3A __denied

    
##_________button click in user interface main____thread & subprocess design 
def temp_click(txt): 
    txt.insert('1.0', "process successful ")

## Change the state in clicking run in root 2

def dataFrameWrite():
    return 0

##Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func