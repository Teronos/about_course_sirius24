import numpy as np
from Optimizer import Optimizer


class RMSProp(Optimizer):
    def __init__(self, learning_rate, beta=0.9, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta = beta
        self.epsilon = epsilon
        self.s_weights = None
        self.s_bias = 0

    def update(self, weights, bias, grad_w, grad_b):
        if self.s_weights is None:
            self.s_weights = np.zeros_like(weights)

        self.s_weights = self.beta * self.s_weights + (1 - self.beta) * grad_w ** 2
        self.s_bias = self.beta * self.s_bias + (1 - self.beta) * grad_b ** 2

        weights -= self.learning_rate * grad_w / (np.sqrt(self.s_weights) + self.epsilon)
        bias -= self.learning_rate * grad_b / (np.sqrt(self.s_bias) + self.epsilon)
        return weights, bias