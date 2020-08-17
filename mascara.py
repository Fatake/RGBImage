import numpy as np
import cv2

IMAGE_NAME = "img/img_512.jpg"

imagen = cv2.imread(IMAGE_NAME)
cv2.imshow("Original",imagen)

# mismo alto y ancho de la imagen 
mask = np.zeros(imagen.shape[:2], dtype="uint8")

# Se busca el centro de la imagen // integer division
(cx, cy) = (imagen.shape[1] // 2, imagen.shape[0] // 2)
# Se dibuja un rectangulo del tamaño de la mascara
cv2.rectangle(mask, (cx-75, cy-75), (cx+75 , cy+75), 255, -1)
cv2.imshow("Mascara",mask)

masked = cv2.bitwise_and(imagen, imagen, mask= mask)
cv2.imshow("Mascara Aplicada", masked)



cv2.waitKey(0)
cv2.destroyAllWindows()
