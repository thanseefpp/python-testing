import numpy as np
import cv2

cascPath = "/Users/mayurgupta/opt/anaconda3/lib/python3.7/site-   packages/cv2/data/haarcascade_frontalface_default.xml"

eyePath = "/Users/mayurgupta/opt/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml"

smilePath = "/Users/mayurgupta/opt/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_smile.xml"

face_cascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier(eyePath)
smile_cascade = cv2.CascadeClassifier(smilePath)

img = cv2.imread('WhatsApp Image 2020-04-04 at 8.43.18 PM.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()