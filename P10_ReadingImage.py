import cv2
import numpy as np
imgorigin = cv2.imread('ChesterStation.jpg', cv2.IMREAD_UNCHANGED) 
imgcolour = cv2.imread('ChesterStation.jpg', cv2.IMREAD_COLOR) 
imggray=cv2.imread('ChesterStation.jpg',cv2.IMREAD_GRAYSCALE)

print("Shape of the origin image is ", imgorigin.shape)
print("Shape of the colour image is ", imgcolour.shape)
print("Shape of the gray image is ", imggray.shape)

print("cv2.imread gives numpy array "+str(type(imgorigin)))
