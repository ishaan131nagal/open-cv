import cv2
import numpy as np

# Load the image
input_image_path = 'IMG.jpg'  # Replace with your image path
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Calculate gradients using Sobel
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude and phase angle
gradient_magnitude, gradient_angle = cv2.magnitude(gradient_x, gradient_y), cv2.phase(gradient_x, gradient_y, angleInDegrees=True)

# Display the original image, gradient magnitude, and gradient angle
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude', gradient_magnitude.astype(np.uint8))
cv2.imshow('Gradient Angle', gradient_angle.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()