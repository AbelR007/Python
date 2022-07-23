# Opens the Image in a new window
# ----------------------------------------------------------------
# Libraries needed
import cv2 as cv
import sys

# Loading the image
img = cv.imread(cv.samples.findFile("python.png"))

# Check if image was loaded or not
if img is None:
    sys.exit("Could not read the image.")

# Shows the image in a new window
cv.imshow("Display Window",img)

# Waits for user keyboard input to close the window
user_input = cv.waitKey(0)

# ----------------------------------------------------------------
# Code by Abel Roy
