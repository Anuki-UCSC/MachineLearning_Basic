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

       

    