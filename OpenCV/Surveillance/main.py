import cv2

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('Frame Window', frame)
    cv2.waitKey(60)

cap.release()
cv2.destroyAllWindows()