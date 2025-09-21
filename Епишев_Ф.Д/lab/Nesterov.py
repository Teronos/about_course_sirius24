import numpy as np

from Optimizer import Optimizer


class Nesterov(Optimizer):

    def __init__(self, learning_rate, gamma=0.9):
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.v_weights = None
        self.v_bias = 0

    def update(self, weights, bias, grad_w, grad_b):
        # Initialize velocity terms if not already initialized
        if self.v_weights is None:
            self.v_weights = np.zeros_like(weights)
            self.v_bias = 0

        # Update gradients based on look-ahead position
        self.v_weights = self.gamma * self.v_weights + self.learning_rate * grad_w
        self.v_bias = self.gamma * self.v_bias + self.learning_rate * grad_b

        # Update weights and bias
        weights -= self.v_weights
        bias -= self.v_bias

        return weights, bias