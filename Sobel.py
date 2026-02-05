import cv2
import numpy as n

img = cv2.imread(r"C:\Users\embed\Desktop\Industrial Vision\archive(3)\wood\test\good\002.png",0)

k=3

result = n.zeros(img.shape,dtype=n.uint8)
x=k//2

for i in range(x,img.shape[0]-x):
    for j in range(x,img.shape[1]-x):
        result[i,j] = img[x][j-1] + imj[x][j]


cv2.imshow("e",result)
cv2.waitKey(0)