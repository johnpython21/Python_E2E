import numpy as np
import matplotlib.pyplot as plt
import cv2
def fun(event,x,y,p,g):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        x1 = str(x)
        y1 = str(y)
        t = x1 + " " + y1
        cv2.putText(black_image,t,(x,y),2,cv2.FONT_HERSHEY_PLAIN,(0,0,255),2)
        cv2.imshow('b_image', black_image)


black_image = np.zeros((640,640,3))
mes_img = cv2.imread('C:\\Users\\DELL\\Downloads\\Computer Vision\\images\\messi.jpg',1) # 0 b&w
cv2.imshow('image',mes_img)
cv2.setMouseCallback('image' , fun)
cv2.waitKey()
cv2.destroyAllWindows()