import cv2
import numpy as np


def sharpen_using_sobel(image):
    # Apply Sobel filters to compute gradients
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    # Convert gradient_magnitude to uint8 data type
    gradient_magnitude = np.uint8(gradient_magnitude)

    # Enhance edges by adding gradient magnitude to the original image
    sharpened = cv2.addWeighted(image, 1.5, gradient_magnitude, 0.5, 0)

    return sharpened


def sharpen_using_laplacian(image):
    # Apply Laplacian filter to compute the second derivative
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # Combine original image and Laplacian for sharpening
    sharpened = image + 0.5 * laplacian

    return sharpened

# Load the image
input_image_path = 'pattern.jpg'  # Replace with your image path
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Perform sharpening using Sobel filter
sharpened_image_sobel = sharpen_using_sobel(image)
sharpened_image_lap = sharpen_using_laplacian(image)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened sobel Image', sharpened_image_sobel)
cv2.imshow('Sharpened Laplacian ',sharpened_image_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()