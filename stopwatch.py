def stopwatch_counter(label):
        def count():
                if stopwatch_running:
                        global stopwatch_counter_num
                        if stopwatch_counter_num==66600:
                                display="Starting..."
                        else:
                                tt = datetime.datetime.fromtimestamp(stopwatch_counter_num) 
                                string = tt.strftime("%H:%M:%S") 
                                display=string 
                        label.config(text=display)
                        label.after(1000, count)
                        stopwatch_counter_num += 1
        count()
