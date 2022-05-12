# DETECÇÃO DE BORDAS EM PYTHON
 Processsamento manual de imagens  passo-a-passo para detecção de bordas utilizando Python
 ## Pré-requesitos
  - [Python 3.9](https://www.python.org/)
  - Instalar as bibliotecas e *frameworks* necessários (`numpy`,`scipy`,`skimage`,`pylab`e `matplotlib`)
  - Ter uma imagem de sua escolha no mesmo diretório do arquivo **main.py**
 ## Instruções de utilização
  - Utilize o arquivo **main.py** para executar o programa
  - O arquivo **Fun.py** possui as funcções utilizadas em **main.py**, não é recomendado alterar o mesmo, entretando o ajuste de contrate pode ter alguns de seus parâmetros alterados, como o coeficiênte de reta do ajuste linear
  - Perceba que é necessário realizar a conversão da imagem para a escala de cinza, essa conversão é feita por uma fórmula padrão
  - Você pode alterar o processo de filtragem e escolher o processamento mais ideal para cada imagem processada (ex: alterar  o ajuste de constraste para expoencial ou linear,  a limiarização para local ou global, etc)
  - Na linha de código 6 : `img = pylab.imread("guitarra.jpg")` você pode alterar a imagem a ser processada, estou disponibilizando duas imagens que utilizei previamente
