from Images import Processar_Dataset as dataset       # importando as funções do processar_dataset
from RedeNeural.Neuronio import Neuronio    # forma de importar a classe Neuronio
from random import Random

# normaliza no range 0, 255
def normalizar(array):
    aux = []
    for i in array:
        aux.append(i/255)
    return aux

# recebe as imagens em grayscale e treina a rede neural
def treinar(neuronio):
    imagens, labels = dataset.format_batch_train(1, 10000)
    contador = len(imagens)/10
    for num in range(0, 10):
        testeI = num*contador
        testeF = testeI + contador

        treinoI1 = 0
        treinoF1 = testeI

        treinoI2 = testeF
        treinoF2 = len(imagens)

        # primeiro conjunto de treino
        for i in range(int(treinoI1), int(treinoF1)):
            output = neuronio.function_limiar(imagens[i])
            if output != labels[i]: # errou a predição
                neuronio.ajustar_pesos(labels[i], output, imagens[i])

        # segundo conjunto de treino
        for i in range(int(treinoI2), int(treinoF2)):
            output = neuronio.function_limiar(imagens[i])
            if output != labels[i]:  # errou a predição
                neuronio.ajustar_pesos(labels[i], output, imagens[i])

        # conjunto de teste
        acertos = 0
        erros = 0
        for i in range(int(testeI), int(testeF)):
            output = neuronio.function_limiar(imagens[i])
            if output != labels[i]:
                erros += 1
            else:
                acertos += 1

        print("Iteração "+str(num)+": Acerto("
              +str(acertos*100/(acertos+erros))+"%) Erro("
              +str(erros*100/(acertos+erros))+"%)\n")



def testar():
    print(1)

# main
if __name__ == '__main__':
    rand = Random()
    pesos = []

    for i in range(0, 1024):
        pesos.append(rand.uniform(0, 1))

    neuronio = Neuronio(1024, pesos, learningRate=0.01, threshold=0)

    treinar(neuronio)
