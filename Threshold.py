import cv2
import numpy as np
img =  cv2.imread(r"C:\Users\embed\Desktop\Industrial Vision\archive(3)\screw\test\manipulated_front\000.png")

print(img)
length = len(img)
print(img[0])
b = len(img[0])

# imgt = np.zeros((length,b,3),dtype = np.uint8)

for i in range(length):
    for j in range(b):
        for k in range(3):
            if (img[i][j][k] >=70):
                img[i][j][k] = 5
            else:
                img[i][j][k] =250

cv2.imshow("rsfrg",img)
cv2.waitKey(0)