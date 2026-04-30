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
        #Capa oculta
        self.Z1=np.dot(X,self.W1) + self.b1
        self.A1=sigmoid(self.Z1)
        #Capa de salida
        self.Z2=np.dot(self.A1,self.W2) + self.b2
        self.A2=sigmoid(self.Z2)

        return self.A2
    
    #Paso hacia atrás
    def backward(self, X, y, learning_rate):
        #Calcular error
        error= y-self.A2
        #Retropropagacion del error
        d_A2=error*sigmoid_prime(self.Z2)
        d_Z1=np.dot(d_A2,self.W2.T)*sigmoid_prime(self.Z1)
        #Actualizar pesos y bias
        self.W2+=np.dot(self.A1.T,d_A2)*learning_rate
        self.b2+=np.sum(d_A2,axis=0,keepdims=True)*learning_rate

        self.W1+=np.dot(X.T,d_Z1)*learning_rate
        self.b1+=np.sum(d_Z1,axis=0,keepdims=True)*learning_rate

    #Entrenamiento
    def train(self, X, y, learning_rate, epochs):
        for epoch in range(epochs):
            y_pred=self.forward(X)
            self.backward(X, y, learning_rate)
            if epoch % 4000 == 0:
                loss = np.mean(np.square(y - y_pred))
                print(f"Epoch {epoch}, Loss:{loss}")


#Test
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

nn = MLP(X, n_hidden=3, n_output=1)
nn.train(X, y, learning_rate=0.1, epochs=10000)

output = nn.forward(X)
print("Predictions after training:")
print(output)