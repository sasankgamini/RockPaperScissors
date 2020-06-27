import keras
import cv2
from keras.models import load_model
import numpy as np

model = load_model('savedRockPaperScissors.h5')

capture=cv2.VideoCapture(0)
while True:
    _, frame = capture.read()
    cv2.rectangle(frame,(625,0),(1250,500),(255,0,0),2)
    grayimage=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ROI = grayimage[0:500,625:1250]
    imgarray=cv2.resize(ROI,(28,28))
    dilatedimg=cv2.dilate(imgarray,(3,3))
    dilatedlist=[dilatedimg]
    dilatedarray=np.array(dilatedlist)
    dilatedarray=dilatedarray/255
    predictions=model.predict(dilatedarray)
    cv2.putText(grayimage, str(np.argmax(predictions[0])),(10,50),cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), 2)
    cv2.imshow('image',grayimage)
    if cv2.waitKey(3) == ord('s'):
        break
capture.release()
cv2.destroyAllWindows()
        
        
        

    
    

    
