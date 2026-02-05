import cv2
import numpy as np

img = cv2.imread(r"C:\Users\embed\Desktop\New folder\IvCode\download.jpg",0) # Replace 'image.jpg' with your image path

if img is None:
    print("Error: Could not read image file")
else:
    blurred_img = cv2.blur(img, (5, 5))
    cv2.imshow('Original', img)
    cv2.imshow('Averaging Blurred', blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
