import cv2
import numpy as np
#Open the image.
img = cv2.imread('C:/Users/PG LAB/PycharmProjects/pythonProject/venv/img22.jpg')
# Apply log transform.
c = 255/(np.log(1+ np.max(img)))
log_transformed = c*np.log(1 + img)
# Specify the data type.
log_transformed = np.array (log_transformed, dtype =  np. uint8)
# Save the output.
cv2.imwrite('log_transformed.jpg', log_transformed)
