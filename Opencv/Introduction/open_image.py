"""
Author: Rohan Singh
12/26/2022
This python module contains the source code required to: read, display and write an image using opencv
"""

#Imports
import cv2 
import sys

#Function to read the image, display it and save it
def read_image(filepath, savepath):

    #Reading an image from the filepath
    img = cv2.imread(cv2.samples.findFile(filepath))
    if img is None:
        sys.exit("Could not read the image.")
    
    #Displaying the image on the opencv window
    cv2.imshow("Display window", img)

    #Saving the image to the savepath
    k = cv2.waitKey(0)
    if k == ord("s"):
        cv2.imwrite(savepath, img)

#Main method
def main():

    #print("Hello World")

    filepath = "/Users/rohansingh/attachments/lol.png"
    savepath = "/Users/rohansingh/desktop/lol.png"

    #Calling the read image method
    read_image(filepath,savepath)



if __name__ == "__main__":
    main()


