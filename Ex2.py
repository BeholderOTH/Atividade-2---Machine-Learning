#Importa o OpenCV e o Matplotlib
import cv2
from matplotlib import pyplot as plt

#Carregar imagem/apontar caminho da imagem
path = '.\my-image.png' #Exemplo de caminho
image = cv2.imread(path)

#Aplica os filtros correspondentes na imagem
blurred_image_media = cv2.blur(image, (5,5)) #Filtro de média
blurred_image_gaussiano = cv2.GaussianBlur(image, (5,5), 0) #Filtro Gaussiano
blurred_image_mediana = cv2.medianBlur(image, 5) #Filtro de mediana

#Plota a imagem suavizada com o filtro de média
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(blurred_image_media, cv2.COLOR_BGR2RGB))
plt.title('Imagem suavizada (Filtro de média)')
#Plota a imagem suavizada com o filtro Gaussiano
plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(blurred_image_gaussiano, cv2.COLOR_BGR2RGB))
plt.title('Imagem suavizada (Filtro Gaussiano)')
#Plota a imagem suavizada com o filtro de mediana
plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(blurred_image_mediana, cv2.COLOR_BGR2RGB))
plt.title('Imagem suavizada (Filtro de mediana)')
plt.show()

