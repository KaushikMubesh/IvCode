import cv2
import numpy as n;

img = cv2.imread(r"C:\Users\kaush\.matplotlib\Desktop\Industrial vision\download.png")
b , g ,r = cv2.split(img)

arr = n.zeros((img.shape[0], img.shape[1]), dtype=n.uint8)
print (img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        arr[i,j] = int(0.299*r[i,j] + .587*g[i,j] + .114*b[i,j])
cv2.imshow("arr",arr)
cv2.waitKey(0)