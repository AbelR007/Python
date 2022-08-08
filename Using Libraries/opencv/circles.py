# Creating circles on Screen
# =================================================
import cv2
import numpy as np

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 100, 100)
    if circles is not None:
        circles = np.round(circles[0,:].astype("int"))
        for (x,y,r) in circles:
            cv2.circle(frame, (x,y), r, (64,255,64),4)
            print(" X = " + str(x) + " Y = " + str(y))
    cv2.imshow("BGR",frame)
    cv2.imshow("GRAY SCALE", gray)
    k = cv2.waitKey(1)
    if (k == 13):
        break

cam.release()
cv2.destroyAllWindows()
# ================================================
# Code by Abel Roy #
