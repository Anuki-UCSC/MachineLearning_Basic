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

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self,min_samples_split=2,max_depth=100,n_feats=None):
        self.min_samples_split=min_samples_split
        self.max_depth=max_depth
        self.n_feats=n_feats
        self.root=None

    
    def fit(self,X,y):
        #grow tree
        self.n_feats=X.shape[1] if not self.n_feats else min(self.n_feats,X.shape[1])
        self.root=self._grow_tree(X,y)

    

    def predict(self,X):





