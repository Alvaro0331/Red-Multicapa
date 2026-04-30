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
        n_features = X.shape[1]

        #Pesos de la capa oculta
        self.W1=np.random.randn(n_features,n_hidden)
        self.b1=np.zeros((1,n_hidden))
        #Pesos de la capa de salida
        self.W2=np.random.randn(n_hidden,n_output)
        self.b2=np.zeros((1,n_output))
        
    #Paso hacia delante
    def forward(self, X):
        a=a
    
    #Paso hacia atrás
    def backward(self, X, y):
        a=a

    #Entrenamiento
    def train(self, X, y, epochs=200):
        a=a