import cv2
import numpy as np
from matplotlib import pyplot as plt

#lendo imagem colorida
img = cv2.imread('./images/cafe.jpg', cv2.IMREAD_COLOR)
#img = cv2.imread('./images/carro.jpg', cv2.IMREAD_COLOR)

# o problema, é que le com RGB ao contrário (BGR), então se tu mostrar a imagem agora fica com cores estranhas, o café fica azul
# por isso, faz a conversão para RGB, e GrayScale
cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1,3,1) # total lines, total cols, position
plt.title('BGR Image')
plt.imshow(img) 

plt.subplot(1,3,2)
plt.title('Color Image')
plt.imshow(cv_rgb,'gray') # show image

plt.subplot(1,3,3)
plt.title('GrayScale Image')
plt.imshow(bw_img,'gray') # show image

plt.show()


# O matplotlib tem esta função direta para mostrar Histograma, mas ai tu não tem os valores se quiser usar para alguma coisa
plt.hist(bw_img.ravel(),256,[0,256])
plt.title('Histogram for gray scale')
plt.show()


# por isso, em muitos casos, é melhor usar a função do OpenCV para calcular o histogram
# cv2.calcHist
# sintax: http://docs.opencv.org/trunk/d1/db7/tutorial_py_histogram_begins.html

plt.subplot(2,1,2)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([cv_rgb],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()