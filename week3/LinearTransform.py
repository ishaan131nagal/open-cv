import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_linear_filter(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate padding based on kernel size
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Pad the image with zeros
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    # Initialize an output array
    filtered_image = np.zeros_like(image)

    # Iterate over the image pixels
    for i in range(image_height):
        for j in range(image_width):
            # Extract a patch from the padded image
            patch = padded_image[i:i + kernel_height, j:j + kernel_width]

            # Apply convolution by element-wise multiplication and summation
            filtered_image[i, j] = np.sum(patch * kernel)

    return filtered_image


# Load an image using OpenCV
image_path = 'C:/Users/PG LAB/PycharmProjects/pythonProject/venv/colosseum.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define a simple averaging kernel (3x3)
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]) / 9

# Apply linear filtering without cv2.filter2D
filtered_image = apply_linear_filter(image, kernel)

# Display the original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')

plt.tight_layout()
plt.show()