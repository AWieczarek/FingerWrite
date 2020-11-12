import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,150,0],np.uint8)
    upper_blue = np.array([120,255,255],np.uint8)

    lower_red = np.array([0,150,0],np.uint8)
    upper_red = np.array([10,255,255],np.uint8)

    # Threshold the HSV image to get only blue colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image

    res_blue = cv.bitwise_and(frame,frame, mask= mask_blue)
    res_red = cv.bitwise_and(frame,frame, mask= mask_red)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask_blue)
    cv.imshow('res',res_blue)


    if cv.waitKey(5) & 0xFF == 27:
        break
cv.destroyAllWindows()
