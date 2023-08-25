import cv2
image = cv2.imread('IMG.jpg')
gaus = cv2.GaussianBlur(image, (7, 7), 10)
cv2.imshow('Original',image)
cv2.imshow('GaussianBlur', gaus)
cv2.imwrite('gaus_Blur.jpg', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()