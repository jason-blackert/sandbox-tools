class Timer:
    """ Purpose : Timer class() intended for millisecond accuracy timing.
        startTime  (int) : vary first startTime (ms) (generally not necessary).
        timeWindow (int) : combines set_new_window(ms) into initialization.
    """
    def __init__(self,
                 startTime=0,  # Will Generally Stay At Zero
                 timeWindow=1000):

        self.StartState      = "START"
        self.InProgressState = "IN-PROGRESS"
        self.OffState        = "OFF"

        self.state = self.OffState
        self.startTime  = startTime  # ms
        self.timeWindow = timeWindow # ms

        self.SCALAR_MS = 1000

    def run(self,current_time):
        """ Purpose : Main Driver for Timer Class
            current_time (int) : feed time.time() in standard units (sec).
        """
        if self.state == self.StartState:
            self.startTime = current_time
            self.state = self.InProgressState
        if self.state == self.InProgressState and (current_time-self.startTime)*self.SCALAR_MS > self.timeWindow:
            self.state = self.OffState

    def set_new_window(self, window):
        self.timeWindow = window # ms

    def off(self):
        self.state = self.OffState

    def start(self):
        self.state = self.StartState

    def isComplete(self):
        if self.state == self.OffState:
            return True
        else:
            return False

if __name__ == "__main__":
    import time

    timer_ms = Timer()
    timer_ms.set_new_window(1000) # ms
    timer_ms.start()

    while True:
        timer_ms.run(current_time=time.time())
        if timer_ms.isComplete():
            t_end = time.time()
            t_elapsed = np.round((t_end-timer_ms.startTime), 2)
            t_refresh = np.round((1/t_elapsed), 2)
            print("Time Elapsed: {} ms | Refresh Rate {} Hz".format((1000*t_elapsed), t_refresh))
            timer_ms.start()