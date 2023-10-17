#Perform transformation using Homography matrix.

import cv2
import numpy as np
im_src = cv2.imread("31180.jpg")
pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])
im_dst = cv2.imread("31180.jpg")
pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])
h, status = cv2.findHomography(pts_src, pts_dst)
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
img = cv2.resize(im_src,(700,650))
img1 = cv2.resize(im_dst,(700,60))
img2 = cv2.resize(im_out,(700,650))
cv2.imshow("Source Image", img)
cv2.imshow("Destination Image", img1)
cv2.imshow("Warped Source Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
