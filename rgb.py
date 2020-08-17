import cv2
import numpy as np

def main():
    IMAGE_NAME = "img/img_512.jpg"

    imagen = cv2.imread(IMAGE_NAME,1)
    cv2.imshow("Original",imagen)

    (B, G, R) = cv2.split(imagen)
    #cv2.imshow("Rojo", R)
    #cv2.imshow("Verde", G)
    #cv2.imshow("Azul", B)
    
    zeros = np.zeros(imagen.shape[:2], dtype ="uint8")
    cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
    cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
    cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))


    negativo(imagen)

    #Escala de Grises 
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gris',gris)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def negativo(imagen):
    #Divides la imagen por canales
    chanel_r = imagen[:,:,2]#Canal R
    chanel_g = imagen[:,:,1]#Canal G
    chanel_b = imagen[:,:,0]#Canal B

    #Optienes las dimenciones
    row, col = chanel_r.shape

    #Generas los canales negativos
    neg_r = np.zeros((row, col), dtype=np.uint8)
    neg_g = np.zeros((row, col), dtype=np.uint8)
    neg_b = np.zeros((row, col), dtype=np.uint8)

    #El negativo es el complemento
    for a in range(0, row):                                            
        for b in range(0, col):                                          
            neg_r[a, b] = 255 - chanel_r[a, b]

    for a in range(0, row):                                            
        for b in range(0, col):                                          
            neg_g[a, b] = 255 - chanel_g[a, b]
    
    for a in range(0, row):                                            
        for b in range(0, col):                                          
            neg_b[a, b] = 255 - chanel_b[a, b]
    
    negativo = imagen
    negativo[:,:,2] = neg_r
    negativo[:,:,1] = neg_g
    negativo[:,:,0] = neg_b

    cv2.imshow('NEGATIVO', negativo)  
        

if __name__ == "__main__":
    main()
