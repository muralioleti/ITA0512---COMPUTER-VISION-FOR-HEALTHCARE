#Perform Edge detection using canny method

import cv2
img = cv2.imread("31180.jpg")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
desired_width = 700
desired_height = 650
img_resized = cv2.resize(edges, (desired_width, desired_height))
cv2.imshow('Canny Edge Detection', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
