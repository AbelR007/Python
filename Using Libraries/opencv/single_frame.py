# Single Frame Display
# =================================================
import cv2
# import sys

cam= cv2.VideoCapture(0) # initilize camera
k=1
while(k <= 8):
    k = k + 1
    ret, frame= cam.read()     # capture single frame
    cv2.imshow("output",frame) # output frame display
    k = cv2.waitKey(1) #& 0xff  # wait for 1ms
    print(">>",k)
    if(k==32): ## ord('x')
        break
cam.release()
cv2.destroyAllWindows()
# ================================================
# Code by Abel Roy #
