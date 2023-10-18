#Perform Sharpening of Image using Laplacian mask with negative center coefficient.

import cv2
import numpy as np
img = cv2.imread("31180.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,1,0], [1,-8,1], [0,1,0]])
sharpened = cv2.filter2D(gray, -1, kernel)
desired_width = 700
desired_height = 650
img_resized = cv2.resize(sharpened, (desired_width, desired_height))
cv2.imshow('Original', gray)
cv2.imshow('Sharpened', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
