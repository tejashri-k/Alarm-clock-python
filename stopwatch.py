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
                
                
