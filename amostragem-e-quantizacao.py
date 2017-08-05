#REF: http://www.rafaelzottesso.com.br/2015/09/amostragem-e-quantizacao/

import numpy as np
import cv2
 
img = cv2.imread('./images/beach-mini.jpg', cv2.IMREAD_COLOR)
 
## Amostragem ##
# Reduzindo a imagem #
# Seleciona uma em cada 2 colunas, e de cada coluna uma a cada duas linhas
n = 2
img_red = img[::n,::n]
 
# Aumentando a imagem #
# Os pixels da imagem atual serão duplucados no eixo x e y. Assim, a imagem volta a ter o tamanho original, mas a partir da imagem reduzida
# Função: np.repeat(matriz, vezes, eixo). O eixo 0 é a altura e 1 a largura.
m = 2
img_aum = np.repeat(img_red, m, axis=0)
img_aum = np.repeat(img_aum, m, axis=1)
 
## Quantização ##
# 255 / 31 = 8,22...
# Assim, teremos uma imagem com 8 tons de cinza. A conta é feita desta forma para descartar a parte decimal dos números e alterar o vetor para que possua apenas 8 valores possíveis.
r = 31
img_qtd = np.uint8(img / r) * r
 
# Mostra uma imagem
# Função: cv.imshow(nome da janela, matriz)
cv2.imshow('original',img)
cv2.imshow('reduzida',img_red)
cv2.imshow('aumentada',img_aum)
cv2.imshow('quantificada',img_qtd)
 
# Funções para o funcionamento correto do python no Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()

