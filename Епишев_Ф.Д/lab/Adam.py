import numpy as np
from Optimizer import Optimizer


class Adam(Optimizer):
    def __init__(self, learning_rate, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m_weights = None
        self.v_weights = None
        self.m_bias = 0
        self.v_bias = 0
        self.beta1_t = 1  # To track (1 - beta1^t)
        self.beta2_t = 1  # To track (1 - beta2^t)

    def update(self, weights, bias, grad_w, grad_b):
        if self.m_weights is None:
            self.m_weights = np.zeros_like(weights)
            self.v_weights = np.zeros_like(weights)

        # Update moments
        self.m_weights = self.beta1 * self.m_weights + (1 - self.beta1) * grad_w
        self.v_weights = self.beta2 * self.v_weights + (1 - self.beta2) * grad_w**2

        self.m_bias = self.beta1 * self.m_bias + (1 - self.beta1) * grad_b
        self.v_bias = self.beta2 * self.v_bias + (1 - self.beta2) * grad_b**2

        # Incrementally update correction terms
        self.beta1_t *= self.beta1
        self.beta2_t *= self.beta2

        # Bias-corrected moments
        m_w_hat = self.m_weights / (1 - self.beta1_t)
        v_w_hat = self.v_weights / (1 - self.beta2_t)

        m_b_hat = self.m_bias / (1 - self.beta1_t)
        v_b_hat = self.v_bias / (1 - self.beta2_t)

        # Update weights and bias
        weights -= self.learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)
        bias -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)

        return weights, bias

