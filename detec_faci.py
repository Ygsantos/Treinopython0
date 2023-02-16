import cv2 # OpenCV
from PIL import Image

from google.colab import drive
drive.mount('/content/drive')

imagem = cv2.imread('/content/drive/MyDrive/Visão Computacional Guia Completo/Images/people1.jpg')

print(imagem.shape)

#cv2.imshow(imagem)
from google.colab.patches import cv2_imshow

imagem = cv2.resize(imagem, (800, 600))

print(cv2_imshow(imagem))


imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
print(cv2_imshow(imagem_cinza))

print(imagem_cinza.shape)

"""## Detecção de faces"""

detector_facial = cv2.CascadeClassifier('/content/drive/MyDrive/Visão Computacional Guia Completo/Cascades/haarcascade_frontalface_default.xml')

deteccoes = detector_facial.detectMultiScale(imagem_cinza)

print(deteccoes)

print(len(deteccoes))

for x, y, w, h in deteccoes:
  #print(x, y, w, h)
  cv2.rectangle(imagem, (x, y), (x + w, y + h), (0,255,255), 5)
print(cv2_imshow(imagem))

"""## Parâmetros haarcascades"""

imagem = cv2.imread('/content/drive/MyDrive/Visão Computacional Guia Completo/Images/people1.jpg')
imagem = cv2.resize(imagem, (800, 600))
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
deteccoes = detector_facial.detectMultiScale(imagem_cinza, scaleFactor=1.09)
for (x, y, w, h) in deteccoes:
  cv2.rectangle(imagem, (x, y), (x + w, y + h), (0,255,0), 5)
print(cv2_imshow(imagem))

imagem = cv2.imread('/content/drive/MyDrive/Visão Computacional Guia Completo/Images/people2.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
deteccoes = detector_facial.detectMultiScale(imagem_cinza, scaleFactor=1.2, minNeighbors=3,
                                             minSize=(32,32), maxSize=(100,100))
for (x, y, w, h) in deteccoes:
  print(w, h)
  cv2.rectangle(imagem, (x, y), (x + w, y + h), (0,255,0), 2)
print(cv2_imshow(imagem))