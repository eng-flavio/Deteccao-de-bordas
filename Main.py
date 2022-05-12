import pylab
import matplotlib.pyplot as plt
import Func as func

#PROCESSAMENTO INICIAL:  CARREGA A IMAGEM E TRANSFORMA A IMAGEM EM ESCALA DE CINZA
img = pylab.imread("guitarra.jpg")
img_gray = 0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]
print(img_gray.shape)
 
#AS FUNÇÕES A SEGUIR FORAM FEITAS EM UM ARQUIVO À PARTE

#AJUSTE DE CONTRASTE
img_gray = func.contraste(2,img_gray,0.005) # 1 =LINEAR, 2 = EXPONENCIAL, 3 =LOGARÍTIMO
#FILTRAGEM
img_gray = func.filtro(1,img_gray) #1=MEDIANA, 2 = GAUSSIANO
#LIMIARIZÇÃO
img_gray = func.limiarizacao(2,img_gray) #1 =GLOBAL, 2 =LOCAL
#FILTRO DE BORDAS
img_gray = func.bordas(1,img_gray) #1 = PREWIT, 2=ROBERTS
#PLOTA A IMAGEM RESULTANTE
pylab.imshow(img_gray,pylab.cm.gray)
plt.show()
