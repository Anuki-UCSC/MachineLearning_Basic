import numpy as np

class SVM:
    def __init__(self, lr=0.001, lambda_param=0.01,n_iters=1000):
        self.lr=lr
        self.lmbp=lambda_param
        self.n_iters=n_iters
        self.w=None
        self.b=None



def predict(self,X):
    linear_output=np.(X,self.w) - self.b
    return np.sign(linear_output)
