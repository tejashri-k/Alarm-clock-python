def stopwatch_counter(label):
        def count():
                if stopwatch_running:
                        global stopwatch_counter_num
                        if stopwatch_counter_num = 66600:
                                display= 'Starting...'
                        else:
                                tt = datetime.datetime.fromtimestamp(stopwatch_counter_num)
                                string = tt.strftime('%H:%M:%S')
                                display = string
                        label.config(text = display)
                        label.after(1000, count)
                        stopwatch_counter_num += 1
        count()

def stopwatch(work):
        if work== 'start':
                global stopwatch running
                stopwatch_running=True
                stopwatch_start.config(state='disabled')
                stopwatch_stop.config(state='enabled')
                stopwatch_reset.config(state='enabled')
                stopwatch_counter(stopwatch_label)
        elif work== 'stop':
                stopwatch_running=False
                stopwatch_start.config(state='enabled')
                stopwatch_stop.config(state='disabled')
                stopwatch_reset.config(state='enabled')
        elif work== 'reset':
                global stopwatch_counter_num
                stopwatch_running=False
                stopwatch_counter_num=66600
                stopwatch_label.config(text='Stopwatch')
                stopwatch_start.config(state='enabled')
                stopwatch_stop.config(state='disabled')
                stopwatch_reset.config(state='disabled')
tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
stopwatch_tab =  Frame(tabs_control)
timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text='Clock')
tabs_control.add(alarm_tab, text='Alarm')
tabs_control.add(stopwatch_tab, text='Stopwatch')
tabs_control.add(timer_tab, text='Timer')
tabs_control.pack(expand = 1, fill = 'both')
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor = 'center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor = 's')
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 10 bold', text = 'Enter alarm time. eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes')
alarm_instructions_label.pack(anchor = 's')
set_alarm_button = Button(alarm_tab, text = 'Set Alarm', command=alarm)
set_alarm.button.pack(anchor = 's')
alarm_status_label = Label(alarm_tab, font = 'calibri 15 bold')
alarm_status_label.pack(anchor= 's')
stopwatch_label = Label(stopwatch_tab, font = 'calibri 40 bold', text = 'Stopwatch')
stopwatch_label.pack(anchor = 'center')
stopwatch_start = Button(stopwatch_tab, text = 'Start', command=lambda:stopwatch('start'))
stopwatch_start.pack(anchor='center')
stopwatch_stop = Button(stopwatch_tab, text = 'Stop', state = 'disabled', command=lambda:stopwatch('stop'))
stopwatch_stop.pack(anchor = 'center')
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch('reset'))
stopwatch_reset.pack(anchor='center')
timer_get_entry = Entry(timer_tab, font='calibri 15 bold')
timer_get_entry.pack(anchor='center')
timer_instructions_label = Label(timer_tab, font= 'calibri 10 bold', text = 'Enter timer time. Eg -> 01:30:30, 01 -> Hour, 30 -> Minutes, 30 -> Seconds')
timer_instructions_label.pack(anchor = 's')
timer_label = Label(timer_tab, font = 'calibri 40 bold', text = 'Timer')
timer_label.pack(anchor='center')
timer_start = Button(timer_tab, text='Start', command=lambda:timer('start'))
timer_start.pack(anchor='center')
timer_stop = Button(timer_tab, text='Stop', state='disabled',command=lambda:timer('stop'))
timer_stop.pack(anchor='center')
timer_reset = Button(timer_tab, text='Reset', state='disabled', command=lambda:timer('reset'))
timer_reset.pack(anchor='center')
clock()
window.mainloop()        
