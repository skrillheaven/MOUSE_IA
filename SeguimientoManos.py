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

        self.mpmanos =mp.solutions.hands
        self.manos = self.mpmanos.Hands(self.mode,self.maxManos,self.Confdeteccion,self.Confsegui)
        self.dibujo = mp.solutions.drawing_utils
        self.tip =[4,8,12,16,20]


    def encontrarmanos(sefl,frame, dibujar = True):
        imgcolor = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.resultados = self.manos.process(imgcolor)


        if sefl.resultados.multi_hand_landmarks:
            for mano in self.resultados.multi_hand_landmarks:
                if dibujar:
                    sefl.dibujo.draw_landmarks(frame,mano, self.mpmanos.HAND_CONNECTIONS)

        return frame