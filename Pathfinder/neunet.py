import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
     return np.sinh(x)/np.cosh(x)

class NeuNet():
    def __init__(self, tp):
        self.tp = tp
        # self.x = np.random.rand(5,1)
        self.h1 = np.random.rand(4,1)
        self.h2 = np.random.rand(4,1)
        self.y = np.random.rand(2,1)
        self.w1 = np.random.rand(4,5)
        self.w2 = np.random.rand(4,4)
        self.w3 = np.random.rand(2,4)
        self.b1 = np.random.rand(4,1)
        self.b2 = np.random.rand(4,1)
        self.b3 = np.random.rand(2,1)
    def initialize(self):
        values = self.tp.split()
        for i in range(len(values)):
            n = float(values[i])
            # W1
            if i <= 4:
                self.w1[0][i-0] = n
                continue
            if i <= 9:
                self.w1[1][i-5] = n
                continue
            if i <= 14:
                self.w1[2][i-10] = n
                continue
            if i <= 19:
                self.w1[3][i-15] = n
                continue
            # W2
            if i <= 23:
                self.w2[0][i-20] = n
                continue
            if i <= 27:
                self.w2[1][i-24] = n
                continue
            if i <= 31:
                self.w2[2][i-30] = n
                continue
            if i <= 35:
                self.w2[3][i-32] = n
                continue
            # W3
            if i <= 39:
                self.w3[0][i-36] = n
                continue
            if i <= 43:
                self.w3[1][i-40] = n
                continue
            # b1
            if i == 44:
                self.b1[0][0] = n
                continue
            if i == 45:
                self.b1[1][0] = n
                continue
            if i == 46:
                self.b1[2][0] = n
                continue
            if i == 47:
                self.b1[3][0] = n
                continue
            # b2
            if i == 48:
                self.b2[0][0] = n
                continue
            if i == 49:
                self.b2[1][0] = n
                continue
            if i == 50:
                self.b2[2][0] = n
                continue
            if i == 51:
                self.b2[3][0] = n
                continue
            # b3
            if i == 52:
                self.b3[0][0] = n
                continue
            if i == 53:
                self.b3[1][0] = n
                continue
    def feed(self, x):
        # self.x = x
        self.h1 = sigmoid(np.dot(self.w1, x)) + self.b1
        self.h2 = sigmoid(np.dot(self.w2, self.h1)) + self.b2
        self.y = sigmoid(np.dot(self.w3, self.h2)) + self.b3
        return (tanh(self.y[0][0]), sigmoid(self.y[1][0]))
