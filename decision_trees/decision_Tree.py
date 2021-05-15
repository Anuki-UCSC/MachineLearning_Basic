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

    def _grow_tree(self,X,y,depth=0):
        n_samples,n_features=X.shape
        n_labels=len(np.unique(y))
        #stopping criteria
        if(depth>=self.max_depth
            or n_labels==1
            or n_samples<self.min_samples_split):
            leaf_value=self._most_common_label(y)
            return Node(value=leaf_value)

        feat_idxs=np.randm.chice(n_features,self.n_feats, replace=False)

        #greedy search
        best_feat, best_thresh=self._best_criteria(X,y,feat_idxs)

    def _best_criteria(self,X,y,feat_idxs):
        best_gain=-1
        split_idx, split_threh=None,None
        for feat_idx in feat_idxs:
            X_column=X[:,feat_idx]
            thresholds=np.unique(X_column)
            for threshold in thresholds:
                gain=self._information_gain(y,X_column, threshold)

                if gain>best_gain:
                    best_gain=gain
                    split_idx=feat_idx
                    split_threh=threshold

        return split_idx, split_threh


        

    def predict(self,X):



    def _most_common_label(self,y):
        counter=Counter(y)
        most_common=counter.most_common(1)[0][0]
        return most_common


