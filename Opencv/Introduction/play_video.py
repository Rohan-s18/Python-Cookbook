"""
Author: Rohan Singh
12/26/22
This python module contains source code to play a input video file on an opncv window
"""

#Imports
import numpy as np
import cv2 as cv


#Function to play the video from the inout filepath
def play_video(filepath):

    #Creating a cpture from the filepath
    cap = cv.VideoCapture(filepath)

    #Going through the frames while the capture is open
    while cap.isOpened():
        flag, frame = cap.read()
        # if the frame is not read correctly flag is False
        if flag == False:
            print("Ops")
            break
    
        #Showing the frames on the opencv window
        cv.imshow('frame', frame)

        #Quitting if 'q' is pressed
        if cv.waitKey(1) == ord('q'):
            break
    
    #Releasing the capture once the video is over (exited)
    cap.release()
    cv.destroyAllWindows()

def main():
    
    #print("Hello World")

    #Filepath for the video
    filepath = "Path to file here"

    #Calling the play video function
    play_video(filepath)

if __name__ == "__main__":
    main()


