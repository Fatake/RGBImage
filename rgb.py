import cv2
import numpy as np

def main():
    IMAGE_NAME = "img/img_512.jpg"

    imagen = cv2.imread(IMAGE_NAME,1)
    cv2.imshow("Original",imagen)

    (B, G, R) = cv2.split(imagen)
    cv2.imshow("Rojo", R)
    cv2.imshow("Verde", G)
    cv2.imshow("Azul", B)

    #Escala de Grises 
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gris',gris)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
