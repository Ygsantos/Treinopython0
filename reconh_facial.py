from PIL import Image
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive
drive.mount('/content/drive')

import zipfile
path = '/content/drive/MyDrive/Visão Computacional Guia Completo/Datasets/yalefaces.zip'
zip_object = zipfile.ZipFile(file=path, mode = 'r')
zip_object.extractall('./')
zip_object.close()

import os
print(os.listdir('/content/yalefaces/train'))


def get_image_data():
    paths = [os.path.join('/content/yalefaces/train', f) for f in os.listdir('/content/yalefaces/train')]
    # print(paths)
    faces = []
    ids = []
    for path in paths:
        # print(path)
        imagem = Image.open(path).convert('L')
        # print(type(imagem))
        imagem_np = np.array(imagem, 'uint8')
        # print(type(imagem_np))
        # print(os.path.split(path)[1])
        id = int(os.path.split(path)[1].split('.')[0].replace('subject', ''))
        # print(id)
        ids.append(id)
        faces.append(imagem_np)

    return np.array(ids), faces

ids, faces = get_image_data()

# threshold: 1.7976931348623157e+308
# radius: 1
# neighbors: 8
# grid_x: 8
# grid_y: 8

lbph_classifier = cv2.face.LBPHFaceRecognizer_create(radius=4, neighbors=14,grid_x=9,grid_y=9) #
lbph_classifier.train(faces, ids)
lbph_classifier.write('lbph_classifier.yml')

lbph_face_classifier = cv2.face.LBPHFaceRecognizer_create()
lbph_face_classifier.read('/content/lbph_classifier.yml')

imagem_teste = '/content/yalefaces/test/subject10.sad.gif'

imagem = Image.open(imagem_teste).convert('L')
imagem_np = np.array(imagem, 'uint8')
print(imagem_np)

previsao = lbph_face_classifier.predict(imagem_np)
print(previsao)

saida_esperada = int(os.path.split(imagem_teste)[1].split('.')[0].replace('subject', ''))
print(saida_esperada)

cv2.putText(imagem_np, 'Pred: ' + str(previsao[0]), (10,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
cv2.putText(imagem_np, 'Exp: ' + str(saida_esperada), (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
print(cv2_imshow(imagem_np))

paths = [os.path.join('/content/yalefaces/test', f) for f in os.listdir('/content/yalefaces/test')]
previsoes = []
saidas_esperadas = []
for path in paths:
  #print(path)
  imagem = Image.open(path).convert('L')
  imagem_np = np.array(imagem, 'uint8')
  previsao, _ = lbph_face_classifier.predict(imagem_np)
  #print(previsao)
  saida_esperada = int(os.path.split(path)[1].split('.')[0].replace('subject', ''))
  #print(saida_esperada)

  previsoes.append(previsao)
  saidas_esperadas.append(saida_esperada)

previsoes = np.array(previsoes)
saidas_esperadas = np.array(saidas_esperadas)



