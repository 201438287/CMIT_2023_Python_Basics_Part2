import cv2
import numpy as np

imgorigin = cv2.imread('France.png', cv2.IMREAD_COLOR) 
Shape=imgorigin.shape
Row=Shape[0]
Col=Shape[1]
#change blue to green
#BGR not RGB
for i in range(Row):
    for j in range(Col):
        if list(imgorigin[i][j])==[146,0,0]:
            imgorigin[i][j]=np.array([0,140,69])
cv2.imwrite("Italy.jpg",imgorigin)
