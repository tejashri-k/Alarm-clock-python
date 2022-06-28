# Alarm-clock-python
def timer_counter(label):
        def count():
                global timer_counter_num
                if timer_counter_num==66600:
                    for i in range(3) :
                            display="Time Is Up"
                            if platform.system() == 'Windows':
                                 winsound.Beep(5000,1000)
                            elif platform.system() == 'Darwin':
                                 os.system('beep -f 5000')
                    timer_running=False
                    timer('reset')
                else:
                        tt = datetime.datetime.fromtimestamp(timer_counter_num)
                        string = tt.strftime("%H:%M:%S")
                        display=string
                        timer_counter_num -= 1
                 label.config(text=display)
                 label.after(1000, count)
                 
        count()   
def time(work):
        if work == 'start':
                global timer_running, timer_counter_num
                timer_running=True
                if timer_counter_num == 66600:
                        timer_time_str = timer_get_entry.get()
                        hours,minutes,seconds= timer_time_str.split(':')
                        minutes = int(minutes)  + (int(hours) * 60)
                        seconds = int(seconds) + (minutes * 60)
                        timer_counter_num = timer_counter_num + seconds
                timer_counter(timer_label)
                timer_start.config(state='disabled')
                timer_stop.config(state='enabled')
                timer_reset.config(state='enabled')
                timer_get_entry.delete(0,END)
         elif work == 'stop':
                timer_running=False
                timer_start.config(state='enabled')
                timer_stop.config(state='disabled')
                timer_reset.config(state='disabled')
                timer_get_entry.config(state='enabled')
                timer_label.config(text = 'Timer')
