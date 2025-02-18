class KalmanFilter1D:
    def __init__(self, x0, P, R, Q):
        """ 
        x0: initial state
        P: variance of state
        R: measurement error
        Q: movement error
        """
        self.x = x0
        self.P = P
        self.R = R
        self.Q = Q

    def update(self, z):
        self.x = (self.P * z + self.x * self.R) / (self.P + self.R)
        self.P = 1. / (1./self.P + 1./self.R)

    def predict(self, u=0.0):
        self.x += u
        self.P += self.Q