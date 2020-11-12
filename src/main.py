import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
colour = 0
old_x = 0
old_y = 0
while(1):

    _, frame = cap.read()
    blurred_frame = cv.GaussianBlur(frame,(5,5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)

    if colour == 0:
        lower = np.array([70,80,0],np.uint8)
        upper = np.array([102,255,255],np.uint8)
    elif colour == 1:
        lower = np.array([0,150,0],np.uint8)
        upper= np.array([10,255,255],np.uint8) 
    elif colour == 2:
        lower = np.array([36,25,25],np.uint8)
        upper= np.array([70,255,255],np.uint8) 
        
    mask = cv.inRange(hsv, lower, upper)    
    res = cv.bitwise_and(frame,frame, mask= mask)

    contours,hierachy=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area = cv.contourArea(contour)
        if area>300:
            #cv.drawContours(frame, contours, -1, (255, 0, 0), 3)
            x, y, w, h = cv.boundingRect(contour) 
            frame = cv.rectangle(frame, (x, y),  (x + w, y + h),  (0, 0, 255), 2)
            cv.line(frame,(int(old_x+(w/2)),int(old_y+(h/2))),(int(x+(w/2)),int(y+(h/2))),(0,0,255),5)
            old_x = x
            old_y = y
            #print(x+(w/2),y+(h/2))

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
