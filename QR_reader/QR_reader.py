import cv2
import numpy as np
from pyzbar.pyzbar import decode

from time import sleep

capture = cv2.VideoCapture(1)
capture.set(3,680)
capture.set(4,480)

while True:
    _,frame = capture.read()
    for barcode in decode(frame):
        print(barcode.data.decode('utf-8'))
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(255,0,255),5)
    cv2.imshow('result',frame)
    sleep(.01)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
