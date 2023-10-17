import cv2

# Load the image
image = cv2.imread('107260.jpg')

# Define the scaling factors for making the image bigger and smaller
bigger_scale = 2.0  # You can adjust this factor to make it bigger
smaller_scale = 0.5  # You can adjust this factor to make it smaller

# Resize the image to make it bigger
bigger_image = cv2.resize(image, None, fx=bigger_scale, fy=bigger_scale, interpolation=cv2.INTER_LINEAR)

# Resize the image to make it smaller
smaller_image = cv2.resize(image, None, fx=smaller_scale, fy=smaller_scale, interpolation=cv2.INTER_LINEAR)

# Display the original, bigger, and smaller images
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
