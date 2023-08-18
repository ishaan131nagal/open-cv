import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backend_bases as backend
image = cv2.imread('C:/Users/PG LAB/PycharmProjects/pythonProject/venv/img22.jpg', cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')

axs[1, 0].plot(hist_original, color='black')
axs[1, 0].set_title('Original Image')
axs[1, 0].set_xlim([0, 256])

axs[0, 1].imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Equalized Image')

axs[1, 1].plot(hist_equalized, color='black')
axs[1, 1].set_title('Histogram(Equalized)')
axs[1, 1].set_xlim([0, 256])

plt.tight_layout

fig.canvas.manager.window.state('zoomed')
plt.show()