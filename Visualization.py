import cv2;

img = cv2.imread(r"C:\Users\kaush\.matplotlib\Desktop\Industrial vision\download.png")
b,g,r = cv2.split(img)
print(b)
print(g)
print(r)
cv2.imshow("a",b)
cv2.imshow("b",g)
cv2.imshow("r",r)
cv2.waitKey(0)


