import numby as np

class LDA:

    def __init__(self,n_components):
        self.n_components=n_components
        self.linear_discriminants=None

    def fit(self,X,y):
        n_features=X.shape[1]
        class_labals=np.unique(y)

    mean_overall=np.mean(x,axis=0)
    s_w=np.zero((n_features,n_features))
    s_b=np.zero((n_features,n_features))

    


       