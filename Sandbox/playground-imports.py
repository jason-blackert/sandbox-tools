import numpy as np
import msvcrt
import time
import cv2
import sys

### IMPORT MODULES ###
sys.path.insert(0, "imports")
from dice import Dice
from timer import Timer

class Sandbox:
    """ Purpose(s) : [REASON]
        Init Vars  : [VARIABLES]
    """
    def __init__(self,
                 refreshRate = 1.0):

        ### MAIN ###
        self.mainCounter = 0
        self.mainState   = True

        ### CAMERA ###
        self.cameraOutput = False
        self.cameraInit   = True

        ### CLASS INITIALIZATION(S) ###
        self.dice     = Dice()
        self.target_framerate = refreshRate
        self.target_fps_ms = (1.0/self.target_framerate)*1000
        self.timer_ms = Timer(timeWindow = self.target_fps_ms)

    def _goodbye(self):
        self.mainState = False

    def _end_of_loop(self):
        """ Contains Contents of All Processes Run At the End of Main. """

        ### LIVE FRAMERATE ###
        self.timer_ms.run(current_time=time.time())
        if self.timer_ms.isComplete():
            t_end = time.time()
            t_elapsed = np.round((t_end-self.timer_ms.startTime), 2)
            t_refresh = np.round((1/t_elapsed), 2)
            print("| Time Elapsed: {} ms | Refresh Rate {} Hz |".format((1000*t_elapsed), t_refresh))
            self.timer_ms.start()

        ### END OF MAIN LOOP ###
        self.mainCounter+=1

    def _keyboard_input(self, pressedKey=None):
        """ Keyboard Input from User. """

        if msvcrt.kbhit():
            if pressedKey == None:
                pressedKey = msvcrt.getch()
            if pressedKey == b'x' or pressedKey == b'X':
                self._goodbye()
            if pressedKey == b'c' or pressedKey == b'C':
                self.cameraOutput = not self.cameraOutput

    def main(self):
        self.timer_ms.start()    # MAIN HAS BEGUN

        while (self.mainState):
            self._keyboard_input()

            self.dice.roll()

            self.camera_input()

            self._end_of_loop()

    def camera_input(self):
        """ A Per-Frame Open-CV Camera Input. """
        if self.cameraOutput and self.cameraInit:
            self.camera1 = cv2.VideoCapture(0)
            self.cameraInit = False

        if self.cameraOutput:
            ret, frame = self.camera1.read()
            cv2.imshow('CAMERA_FRAME',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.mainState=False

        if not self.cameraInit:
            if not self.cameraOutput and self.camera1.isOpened():
                self.camera1.release()
                cv2.destroyAllWindows()
                self.cameraInit = True

if __name__ == "__main__":
    playground = Sandbox(refreshRate=1.0)
    playground.main()