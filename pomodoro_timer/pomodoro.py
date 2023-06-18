import time 





class Pomodoro:
    def __init__(self):
        self.begin = 0
        self.poms_completed = 0

        self.end = 0

    def current_time(self):
        elapsed = round(time.time()) - self.begin
        return elapsed
    
    def pause_timer(self):
        pass 

    def stop_timer(self):
        pass 

    def start_timer(self):
        self.begin = time.time()

    def original_time(self):
        return self.begin 
    

    def timer_end(self, end):
        pass

    

    

