import cv2

img_grayscale = cv2.imread('C:/Users/OSLAB/Downloads/download.jpg',0)
cv2.imshow('graycsale image', img_grayscale)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('C:/Users/OSLAB/Downloads/grayscale.jpg', img_grayscale)
