import numpy as np
from decision_tree import DecisionTree
from collections import Counter



class RandomForest:
    def __init__(self,n_trees=100,min_samples_split=2, max_depth=100, n_feats=None):
        self.n_trees=n_trees
        self.min_samples_split=min_samples_split
        self.max_depth=max_depth
        self.n_feats=n_feats
        self.trees=[]

