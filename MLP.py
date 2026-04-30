import numpy as np

#Función de activación sigmoide y su derivada
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    s = sigmoid(z)
    return s * (1.0 - s)


#Red neuronal multicapa (MLP)
class MLP:
    def __init__(self, X, n_hidden, n_output):
        a=a
    
    #Paso hacia delante
    def forward(self, X):
        a=a
    
    #Paso hacia atrás
    def backward(self, X, y):
        a=a

    #Entrenamiento
    def train(self, X, y, epochs=200):
        a=a