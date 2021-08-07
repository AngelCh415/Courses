from cv2 import cv2
import numpy as np
from numpy.core.fromnumeric import var
varGauss = 3
varKernel = 3
original = cv2.imread('monedas.jpg')
gris = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
#varGauss is a matrix
gauss= cv2.GaussianBlur(gris,(varGauss, varGauss), 0)
canny = cv2.Canny(gauss,60,100)
kernel = np.ones((varKernel,varKernel),np.uint8)
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
contornos, jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Coins found {}".format(len(contornos)))
cv2.drawContours(original,contornos,-1,(0,0,255),2)
#Show
cv2.imshow("Gray",gris)
cv2.imshow("Gauss", gauss)
cv2.imshow("Canny", canny)
cv2.imshow("Close", cierre)
cv2.imshow("Final",original)
cv2.waitKey(0)