import cv2
image = cv2.imread('IMG.jpg')
gaus = cv2.GaussianBlur(image,(7,7),1)
sub = cv2.subtract(image,gaus) #subtract used for sharpening
sharpen = cv2.add(image,sub)
cv2.imshow('Original Image',image)
cv2.imshow('Gaussian blurred image',gaus)
cv2.imshow('Sharpened image',sharpen)
cv2.imwrite('gaus_sharp.jpg',sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()