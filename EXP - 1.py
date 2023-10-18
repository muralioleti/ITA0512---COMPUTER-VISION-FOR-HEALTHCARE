import cv2
img=cv2.imread('31180.jpg')
cv2.imshow('original',img)
cv2.waitKey(0)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0)   
cv2.destroyAllWindows()
