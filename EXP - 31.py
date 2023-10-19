import cv2
import numpy as np
image = cv2.imread('101692.png')  
kernel = np.ones((5, 5), np.uint8)  
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
