import cv2
import numpy as np

# Load the image (make sure it's a binary image)
image = cv2.imread('101687.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel for erosion (a 3x3 square kernel in this example)
kernel = np.ones((3, 3), np.uint8)

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
