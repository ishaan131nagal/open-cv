
import cv2

# path
#path = r'C:/Users/OSLAB/Downloads/park.jpg'

# Reading an image in default mode
image = cv2.imread('C:/Users/OSLAB/Downloads/park.jpg')

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (5, 5)

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (150, 150)

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)