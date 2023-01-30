"""
Author: Rohan Singh
12/26/22
This python module contains source code to Capture videos using OpenCV from a camera, in this case it will be the built-in web camera.
"""

#Imports
import numpy as np
import cv2 as cv


#This function will capture the video
def capture_video():

    #Using the video capture function
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    
    #Continously capture it
    while True:
        flag, frame = cap.read()
        
        #if frame is not read correctly flag is False
        if flag == False:
            print("uh oh")
            break

        #Display the web cam footage
        cv.imshow("Your Video",frame)

        #Quitting when 'q' is pressed
        if cv.waitKey(1) == ord('q'):
            break

    #Releasing the capture
    cap.release()
    cv.destroyAllWindows()


#Main method
def main():
    #print("Hello World!")

    #Calling the capture video function
    capture_video()

if __name__ == "__main__":
    main()


