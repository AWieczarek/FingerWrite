import cv2 as cv
import numpy as np


cv.namedWindow('frame')

cap = cv.VideoCapture(0)

noise = np.array([0], np.uint8)
colorsL = np.array([0,0,0], np.uint8)
colorsU = np.array([0,0,0], np.uint8)
colors = np.array([0,0,0], np.uint8)
def nothing(x):
    pass

def getMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # list of selected coulours
        print("x: ", x,"y: ", y)
        global colorsL
        global colorsU
        global colors
        global noise
        for i in range(3):
            colors[i] = frame[y,x,i]
            a = int(frame[y,x,i]) - int(noise)
            b = int(frame[y,x,i]) + int(noise)
            if b > 255:
                colorsL[i] = frame[y,x,i] - noise
                colorsU[i] = 255
            elif a < 0:
                colorsL[i] = 0
                colorsU[i] = frame[y,x,i] + noise
            else:
                colorsU[i] = frame[y,x,i] + noise
                colorsL[i] = frame[y,x,i] - noise
        cv.setTrackbarPos("B", "frame", colors[2])
        cv.setTrackbarPos("G", "frame", colors[1])
        cv.setTrackbarPos("R", "frame", colors[0])

        print("lower" , colorsL)
        print("upper" , colorsU)

cv.setMouseCallback('frame', getMouse)
cv.createTrackbar('R', 'frame', 0, 255, nothing)
cv.createTrackbar('G', 'frame', 0, 255, nothing)
cv.createTrackbar('B', 'frame', 0, 255, nothing)
cv.createTrackbar('Noise', 'frame', 0, 255, nothing)

while 1:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    noise = cv.getTrackbarPos("noise", "frame")


    mask = cv.inRange(hsv, colorsL, colorsU)    
    cv.imshow('frame',hsv)
    cv.imshow('mask', mask)
    r = cv.getTrackbarPos('R','frame')
    g = cv.getTrackbarPos('G','frame')
    b = cv.getTrackbarPos('B','frame')
    
    if cv.waitKey(5) & 0xFF == 27:
        break
cv.destroyAllWindows()
