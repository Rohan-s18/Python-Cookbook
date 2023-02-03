"""
Author: Rohan Singh
February 2, 2023
Code for Human Detection using OpenCV hog
"""

# Imports
import cv2

# Load the pre-trained HOG (Histogram of Oriented Gradients) human detection model
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Load the video or image
cap = cv2.VideoCapture("video.mp4")

# Loop over each frame
while True:
    # Read a frame
    ret, frame = cap.read()

    # Check if the video is finished
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Detect humans using the HOG model
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(32, 32), scale=1.05)

    # Draw bounding boxes around the detected humans
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Human Detection", frame)

    # Break the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
