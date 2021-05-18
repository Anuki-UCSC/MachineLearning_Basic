import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

from random_forest import RandomForest

def accuracy(y_true, y_pred):
    accuracy=np.sum(y_true==y_pred) / len(y_true)
    return accuracy

