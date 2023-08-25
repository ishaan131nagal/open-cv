import cv2

# Load the image in grayscale
image_path = 'brightspot.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Find the minimum and maximum pixel values and their corresponding locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image)

# Draw a red circle around the brightest spot
brightest_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.circle(brightest_image, max_loc, 10, (0, 0, 255), 2)  # Draw a red circle

# Display the original image and the image with the brightest spot highlighted
cv2.imshow('Original Image', image)
cv2.imshow('Brightest Spot', brightest_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
