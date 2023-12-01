import cv2 
from matplotlib import pyplot as plt

#Carregar imagem/Apontar o caminho da imagem
path = '.\my-image.png' #Exemplo de caminho 
image = cv2.imread(path)

#Converte a imagem para a escala cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Normaliza a imagem para o intervalo [0,1]
normalized_image = gray_image / 255.0

#Verifica se a imagem não é um arquivo "vazio"
if image is not None:
    #Obtém dimensões da imagem
    height, width, channels = image.shape

    properties = [
        ('Altura', image.shape[0]), #Lê a altura da imagem
        ('Largura', image.shape[1]), #Lê a largura da imagem
        ('Canais de cor', image.shape[2]), #Lê os canais de cores da imagem
        ('Tipo de dados', image.dtype), #Lê o tipo de dados da imagem
        ('Tom mínimo de cinza', normalized_image.min()), #Lê o tom mínimo de cinza da imagem
        ('Tom médio de cinza', normalized_image.mean()), #Lê o tom médio de cinza da imagem
        ('Tom máximo de cinza', normalized_image.max()) #Lê o tom máximo de cinza da imagem
    ]

    #Lista todas as propriedades e seus "atributos"
    for propName, propAtt in properties:
        print(f"{propName}: {propAtt}")
