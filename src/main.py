import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
colour = 0
while(1):

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    if colour == 0:
        lower = np.array([70,86,0],np.uint8)
        upper = np.array([121,255,255],np.uint8)
    elif colour == 1:
        lower = np.array([0,150,0],np.uint8)
        upper= np.array([10,255,255],np.uint8) 
    elif colour == 2:
        lower = np.array([36,25,25],np.uint8)
        upper= np.array([70,255,255],np.uint8) 
        
    mask = cv.inRange(hsv, lower, upper)    
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    if cv.waitKey(1) & 0xFF == ord('b'):
            colour = 0

    if cv.waitKey(1) & 0xFF == ord('r'):
        colour = 1
    
    if cv.waitKey(1) & 0xFF == ord('g'):
        colour = 2

    


    if cv.waitKey(5) & 0xFF == 27:
        break
cv.destroyAllWindows()
