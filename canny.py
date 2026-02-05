import cv2
import numpy as np

img = cv2.imread(r"C:\Users\embed\Desktop\New folder\IvCode\down.jpg",0)

edges = cv2.Canny(img, 100, 200)
print(np.count_nonzero(edges))
k=cv2.Sobel(img,100,200)
print(np.count_nonzero(k))
cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)
