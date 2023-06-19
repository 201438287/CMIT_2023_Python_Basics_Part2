import cv2
import numpy as np

# Read the image
img = cv2.imread("ChesterStation.jpg", 0)
cv2.imwrite("PictureGrayscale.jpg",img)
# Thresholding the image
# convert to binary image
(thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

cv2.imwrite("PictureBinary.jpg",img_bin)

#invert all colour
img = cv2.imread("ChesterStation.jpg", cv2.IMREAD_UNCHANGED)
cv2.imwrite("PictureInvert.jpg",255-img)
