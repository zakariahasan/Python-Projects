import cv2
import numpy as np
from tensorflow.keras.models import load_model



capture = cv2.VideoCapture(4)
capture.set(3,640)
capture.set(3,340)

##################
# Load the Model
model = load_model('my_model')
threshold =0.7
while True:
    _, frame =capture.read()
    frame = np.asarray(frame)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.resize(frame_gray,(32,32))
    frame_gray = frame_gray.reshape(1,32,32,1)
    class_Name =model.predict_classes(frame_gray)
    probability= model.predict(frame_gray)
    probability=np.amax(probability)
    if probability > threshold:
        #print(class_Name)
        #print(probability)
        cv2.putText(frame,str(class_Name)+' '+str(probability),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,225),1)
    cv2.imshow('Frame',frame)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyWindow()
