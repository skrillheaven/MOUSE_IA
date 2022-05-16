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


    if len(lista) !=0:
        x1,y1 =lista[8][1:]
        x2,y2 = lista[12][1:]
        
    dedos=detector.dedosarriba()
    cv2.rectangle(frame,(cuadro,cuadro),(anchocam - cuadro,altocam-cuadro),(0,0,0),2)

    if dedos[1]==[1] and dedos [2] ==0:

        x3= np.interp(x1,(cuadro,anchocam-cuadro),(0,anchopanta))
        y3 =np.interp(y1,(cuadro,altocam-cuadro),(0,altopanta))
