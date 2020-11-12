import cv2 as cv
import numpy as np
import pyautogui

cap = cv.VideoCapture(0)
colour = 0
old_x = 0
old_y = 0

while(1):

    _, frame = cap.read()
    frame = cv.flip(frame,1)
    blurred_frame = cv.GaussianBlur(frame,(5,5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)

    lower = np.array([70,80,0],np.uint8)
    upper = np.array([122,255,255],np.uint8)

        
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
            pyautogui.moveTo(int((x+(w/2))*3),int((y+(h/2))*2.5))
            #print(x+(w/2),y+(h/2))

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    if cv.waitKey(5) & 0xFF == 27:
        break

cv.destroyAllWindows()
