import cv2
image_path = '101692.jpg'
image = cv2.imread(image_path)
angle_degrees = 45  # Adjust the angle as needed
# Calculate the image center
height, width = image.shape[:2]
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle_degrees, scale=1.0)
rotated_clockwise = cv2.warpAffine(image, rotation_matrix, (width, height))
rotated_counterclockwise = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Clockwise Rotated Image', rotated_clockwise)
cv2.imshow('Counterclockwise Rotated Image', rotated_counterclockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
