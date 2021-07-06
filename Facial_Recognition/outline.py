import cv2

image = cv2.imread('contorno.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(gray,100,255, cv2.THRESH_BINARY) #_ is like a variable but python ignored it
#findCountours we need the image in gray, 2 methods Aprox_None and aprox_simple
outlines, hierarchy = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#drawcontours
cv2.drawContours(image, outlines, -1,(0,255,0),3) #With -1 show all the contours
#Show image
cv2.imshow('image', gray) 
cv2.imshow('Original', image)
cv2.imshow('Umbral', umbral)
cv2.waitKey(0) #1 fluid like a video or camera, 0 for image static 
cv2.destroyAllWindows()
