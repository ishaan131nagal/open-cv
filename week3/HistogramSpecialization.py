import cv2
import numpy as np
import matplotlib.pyplot as plt

input_image = cv2.imread(r"input_img.jpg", 0)
target_image = cv2.imread(r"target_img.jpg", 0)

input_hist, _ = np.histogram(input_image.flatten(), bins=256, range=[0, 256])
target_hist, _ = np.histogram(target_image.flatten(), bins=256, range=[0, 256])

input_cdf = input_hist.cumsum()
target_cdf = target_hist.cumsum()

input_cdf_normalized = input_cdf / input_cdf[-1]
target_cdf_normalized = target_cdf / target_cdf[-1]

mapping_function = np.interp(input_cdf_normalized, target_cdf_normalized, np.arange(256))

matched_image = mapping_function[input_image]

matched_hist, _ = np.histogram(matched_image.flatten(), bins=256, range=[0, 256])

plt.figure(figsize=(12, 16))

plt.subplot(3, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Input Image')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.plot(input_hist, color='blue')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(3, 2, 3)
plt.imshow(target_image, cmap='gray')
plt.title('Target Image')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.plot(target_hist, color='green')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(3, 2, 5)
plt.imshow(matched_image, cmap='gray')
plt.title('Matched Image')
plt.axis('off')

plt.subplot(3, 2, 6)
plt.plot(matched_hist, color='red')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()