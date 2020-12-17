import numpy as np
import time
import cv2
import sys
import os

class Camera:

    def view(self):

        try:
            self.camera = cv2.VideoCapture(0)

            while(True):
                # Capture frame-by-frame
                ret, frame = self.camera.read()
                # Display the resulting frame
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except KeyboardInterrupt:
            # When everything done, release the capture
            self.camera.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam = Camera()
    webcam.view()