import cv2
import numpy as np
import SeguimientoManos as sm
import autopy

anchocam, altocam=640,480
cuadro =100
anchopanta,altopanta =autopy.screensize()
sua=5
pubix,pubiy =0,0
cubix,cubiy =0,0



cap =cv2.VideoCapture(0)
cap.set(3,anchocam)
cap.set(4,altocam)


