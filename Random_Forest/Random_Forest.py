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

    def fit(self,X,y):
        self.tree=[]
        for _ in range(self.n_trees):
            tree=DecisionTree(min_samples_split=self.min_samples_split,
            max_depth=self.max_depth,n_feats=self.n_feats)
        X_sample,y_sample=bootstrap_sample(X,y)
        tree.fit(X_sample,y_sample)
        self.n_trees.append(tree)

