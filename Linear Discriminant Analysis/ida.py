import numby as np

class LDA:

    def __init__(self,n_components):
        self.n_components=n_components
        self.linear_discriminants=None

        