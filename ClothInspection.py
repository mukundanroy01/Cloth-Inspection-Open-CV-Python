import cv2
import numpy as np

img = cv2.imread("holes.jpg")

kernel = np.ones((5,5),np.uint8)

while True:
    cv2.imshow("Image",img)

    imgCanny = cv2.Canny(img,521,521)
    imgDilate = cv2.dilate(imgCanny,kernel,iterations=4)
    imgErode = cv2.erode(imgDilate,kernel,iterations=5)

    contours,hierarchy = cv2.findContours(imgErode,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>100:
            x,y,w,h = cv2.boundingRect(cnt)
            imgResult = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)

    cv2.imshow("Canny",imgCanny)
    cv2.imshow("Dilated",imgDilate)
    cv2.imshow("Eroded", imgErode)
    cv2.imshow("Result",imgResult)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break