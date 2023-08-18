import cv2
import numpy as np
# Open the image.
img = cv2.imread('C:/Users/PG LAB/PycharmProjects/pythonProject/venv/img22.jpg')
#Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # Apply gamma correction.
    gamma_corrected = np.array (255*(img / 255)** gamma, dtype = 'uint8')
    # Save edited images.
    cv2.imwrite('gamma_transformed' + str(gamma)+'.jpg', gamma_corrected)