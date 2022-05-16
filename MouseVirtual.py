import cv2
from matplotlib.transforms import Bbox
import numpy as np
import SeguimientoManos as sm
import autopy

anchocam, altocam=640,480
cuadro =100
anchopanta,altopanta =autopy.screen.size()
sua=5
pubix,pubiy =0,0
cubix,cubiy =0,0



cap =cv2.VideoCapture(0)
cap.set(3,anchocam)
cap.set(4,altocam)

detector =sm.detectormanos(maxManos=1) #una sola mano

while True:
    ret,frame =cap.read()
    frame = detector.encontrarmanos(frame)
    lista,bbox = detector.encontrarposicion(frame)


