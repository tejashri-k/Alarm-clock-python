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
                
                
