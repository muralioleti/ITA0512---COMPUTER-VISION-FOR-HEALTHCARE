import cv2
import numpy as np

# Load the image
image = cv2.imread('31180.jpg')

# Define four points in the original image and their corresponding positions in the transformed image
original_points = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
transformed_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Calculate the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(original_points, transformed_points)

# Apply the perspective transformation to the image
perspective_image = cv2.warpPerspective(image, perspective_matrix, (300, 300))

# Display the transformed image
cv2.imshow('Perspective Transformed Image', perspective_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
