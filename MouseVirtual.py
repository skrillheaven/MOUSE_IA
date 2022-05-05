import math
import cv2
import mediapipe
import time


class detectormanos():
    def __init__(self,mode=False, maxManos =2, Confdeteccion =0.5,Confsegui=0.5):
        self.mode =mode
        self.maxManos =maxManos
        self.Confdeteccion = Confdeteccion
        self.Confsegui = Confsegui

        