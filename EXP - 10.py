import cv2
import numpy as np
image=cv2.imread('107260.jpg')
dx=100
dy=100
translation_matrix=np.float32([[1,0,dx],
                               [0,1,dy]])
moved_image=cv2.warpAffine(image,translation_matrix,(image.shape[1],image.shape[0]))
cv2.imshow('Moved Image',moved_image)
cv2.waitKey(0)
cv2.detroyAllWindows()
