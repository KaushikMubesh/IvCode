import cv2
import numpy as n

img = cv2.imread(r"C:\Users\kaush\.matplotlib\Desktop\Industrial vision\down.jpg",0)

k=int(input("only odd"))
kernel = n.ones((k,k),dtype = n.uint8)
kernel = kernel/(k*k)

result = n.zeros(img.shape,dtype=n.uint8)
x=k//2

for i in range(x,img.shape[0]-x):
    for j in range(x,img.shape[1]-x):
        win = img[i-x:i+x+1,j-x:j+x+1]
        mean = n.sum(win*kernel)
        result[i,j] = int(mean)


cv2.imshow("e",result)
cv2.waitKey(0)