import numpy as np
import msvcrt
import time
import cv2
import sys
import os

### MODULES ###
sys.path.insert(0, "imports")
from dice import Dice
from timer import Timer

class Sandbox:
    """ Purpose(s) : [REASON]
        Init Vars  : [VARIABLES]
    """
    def __init__(self):

        ### MAIN() ###
        self.mainState = True
        self.mainCounter = 0
        self.cameraOutput = False
        self.cameraInit = True

        ### END_OF_LOOP() ###
        self.start_time_live = 0
        self.end_time_lime   = 0
        self.target_framerate = 100.0
        self.target_fps_ms    = (1.0 / self.target_framerate) * 1000

        ### CLASS INITIALIZATION(S) ###
        self.dice = Dice()
        self.timer_main = Timer(timeWindow=1000)

    def _goodbye(self):
        self.mainState = False

    def _end_of_loop(self):
        """ Contains Contents of All Processes Run At the End of Main. """

        ### LIVE FRAMERATE ###
        self.end_time_live = time.time()
        time_taken = self.end_time_live - self.start_time_live
        self.start_time_live = self.end_time_live

        self.timer_main.run(current_time=time.time())
        if self.timer_main.complete():
            framerate_live = self.target_framerate / (time_taken+1)
            print("App Refresh Rate: ~{} Hz".format(round(framerate_live, 2)))
            self.timer_main.start()

        ### END OF MAIN LOOP ###
        self.mainCounter+=1

    def _keyboard_input(self, pressedKey=None):
        """ Keyboard Input from User. """

        if msvcrt.kbhit():
            if pressedKey == None:
                pressedKey = msvcrt.getch()
            if pressedKey == b'x':
                self._goodbye()
            if pressedKey == b'X':
                self._goodbye()
            if pressedKey == b'c':
                self.cameraOutput = not self.cameraOutput
            if pressedKey == b'C':
                self.cameraOutput = not self.cameraOutput

    def main(self):
        self.timer_main.start()    # MAIN HAS BEGUN

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
    playground = Sandbox()
    playground.main()