from tkinter import *
from tkinter.ttk import *
import datetime
import platform
try:
        import winsound
        type='windows'
except:
        import os
        type='other'
window = Tk()
window.title("Clock")
window.geometry('500x250')
stopwatch_counter_num = 66600
stopwatch_running = False
timer_counter_num = 66600
timer_running = False
def clock():
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 11 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        date_label.config(text= date)
        time_label.after(1000, clock)