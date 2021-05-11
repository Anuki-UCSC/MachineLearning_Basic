import numpy as np

class LogisticRegrssion:

    def __init__(self,lr=0.001,n_iters=1000):
        #  why the learning rate(lr) is so low?
        self.lr=lr
        self.n_iters =n_iters
        self.bias=None
        self.weights=None

    def fit(self,X,y):
        # init parameters
        n_samples,n_features=X.shape
        self.weight=np.zeros(n_features)
        self.bias=0

 #gradient 
        for _ in range(self.n_iters):
            linear_model=np.dot(X,self.weights) + self.bias
            y_predicted=self.sigmoid(linear_model)

        dw=(1/n_samples)+ np.dot(X.T,(y_predicted - y))
        db=(1/n_samples)+np.sum(y_predicted -y)

        self.weights -= self.lr +dw
        self.bias -= self.lr +db


    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))
       

    