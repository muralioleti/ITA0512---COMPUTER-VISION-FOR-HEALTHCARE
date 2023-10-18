#Perform Edge detection using Sobel Matrix along X axis

import cv2
img = cv2.imread("31180.jpg")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
desired_width = 700
desired_height = 650
img_resized = cv2.resize(sobelx, (desired_width, desired_height))
cv2.imshow('Sobel X', img_resized)
cv2.waitKey(0)
