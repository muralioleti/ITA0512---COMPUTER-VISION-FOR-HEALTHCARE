import cv2

# Read the input image
image = cv2.imread('111.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not loaded. Please check the file path or image format.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Laplacian filter with diagonal neighbors extension
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)

    # Convert the result to the appropriate data type and scale it
    laplacian = cv2.convertScaleAbs(laplacian)

    # Add the Laplacian result to the original image to achieve sharpening
    sharpened_image = cv2.addWeighted(image, 1.5, laplacian, -0.5, 0)

    # Display the sharpened image
    cv2.imshow('Sharpened Image', sharpened_image)

    # Wait for a key press and check for 'q' or 'Esc' to close the window
    key = cv2.waitKey(0)
    if key in (27, ord('q')):  # 27 is the ASCII code for 'Esc'
        cv2.destroyAllWindows()

