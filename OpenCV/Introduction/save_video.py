"""
Author: Rohan Singh
12/26/22
This python module contains source code to save a video from the webcam and saving it to a file with a specific filepath
"""

#Imports
import numpy as np
import cv2 as cv

#Function to dave the video to a given location
def save_video(filepath):

    #Opening the webcam
    cap = cv.VideoCapture(0)

    #Defining the codec and create VideoWriter object to save the video
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

    #Saving the frames individually while the camera is open
    while cap.isOpened():
        flag, frame = cap.read()
        if flag == False:
            print("Ops")
            break
        #Writing the frame
        out.write(frame)
        cv.imshow('footage', frame)

        #Quitting when 'q' is pressed
        if cv.waitKey(1) == ord('q'):
            break

    #Releasing the capturer and writer objects once the task is done 
    cap.release()
    out.release()
    cv.destroyAllWindows()


#Main method
def main():
    
    #print("Hello World!")

    #Filepath of the video
    filepath = 'output.avi'
    save_video(filepath)

if __name__ == "__main__":
    main()










