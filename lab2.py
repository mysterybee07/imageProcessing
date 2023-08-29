import cv2

# Load an image from file
image = cv2.imread('lab1.jpg', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (adjust this value as needed)
threshold_value = 128

# Apply binary thresholding
ret, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Save the binary image
cv2.imwrite('output_binary_image.jpg', binary_image)

# Display the original and binary images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
