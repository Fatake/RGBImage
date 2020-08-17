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
    
    negativo(imagen)

    #Escala de Grises 
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gris',gris)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def negativo(imagen):
    row, col = imagen.shape 
    negativo = np.zeros((row, col), dtype=np.uint8)

    for a in range(0, row):                                            
        for b in range(0, col):                                          
            negativo[a, b] = 255 - img[a, b]        

    cv2.imshow('NEGATIVO', negativo)  
        

if __name__ == "__main__":
    main()
