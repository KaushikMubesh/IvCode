import cv2
import numpy as n;
import random
import math

img = cv2.imread(r"C:\Users\embed\Desktop\New folder\IvCode\download.png")
b , g ,r = cv2.split(img)

arr = n.zeros((img.shape[0], img.shape[1]), dtype=n.uint8)
print (img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        arr[i,j] = int(0.299*r[i,j] + .587*g[i,j] + .114*b[i,j])

arr1 = n.zeros((img.shape[0], img.shape[1]), dtype=n.uint8)
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        arr1[i][j] = random.randint(1, 255)
        # print(random.randint(1, 255))
# # cv2.imshow("arr",arr)
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        arr1[i][j] = int((1/((2*3.14*30*30)**(.5)) * math.exp((-((arr1[i][j]-0)**2))/(2*30*30))))
        print(int((1/((2*3.14*30*30)**(.5)) * math.exp((-((arr1[i][j]-0)**2))/(2*30*30)))))


cv2.imshow("arr",arr1)
cv2.waitKey(0)