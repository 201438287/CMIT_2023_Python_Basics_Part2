import cv2
import numpy as np

imgorigin = cv2.imread('France.png', cv2.IMREAD_COLOR) 
Shape=imgorigin.shape
Row=Shape[0]
Col=Shape[1]
X=set()
for i in range(Row):
    for j in range(Col):
        exit()
        s=""
        for k in imgorigin[i][j]:
           s=s+","+str(k)
        X.add(s)
#use set to delte repeating element
print(X)
