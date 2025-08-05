import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import time

cap = cv2.VideoCapture(0) # 0 means your web cam
c = 1

while True:
    res,pixel_values = cap.read()
    if res == True:
        t = 'Frame : '+ str(c)
        f = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(pixel_values,t,(50,70),2,f,(0,0,255),2)
        time.sleep(0.01)
        cv2.imshow('Frames',pixel_values)
        cv2.imwrite('C:\\Users\\DELL\\Downloads\\Computer Vision\\images\\outcomes\\'+str(c)+'.jpg',pixel_values)
        c = c + 1
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()