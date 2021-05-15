import numpy as np

def entropy(y):
    # find the number of occurances
    hist = np.bitcount(y) 
    #p(x)
    ps=hist/len(y)
    return -np.sum([p * np.log2(p) for p in ps if p >0])


class Node:
    def __init__(self,feature=None,threshod=None, left=None, right=None,*,value=None):
        self.feature=feature
        self.threshold=threshod
        self.left=left
        self.right=right
        self.value=value
        