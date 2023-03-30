#  Alternate Code for Human Detector

#  Importing Opencv
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('/Users/rohansingh/github_repos/ECSE488_Project/Python Code/haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed

    # Break the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture object
cap.release()
