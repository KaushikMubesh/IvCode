import cv2

img = cv2.imread(r"C:\Users\kaush\.matplotlib\Desktop\Industrial vision\down.jpg",0)

edges = cv2.Canny(img, 100, 200)

cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)
