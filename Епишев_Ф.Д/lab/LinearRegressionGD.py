import numpy as np
from Adam import Adam
from Nesterov import Nesterov
from RMSProp import RMSProp
from SGD import SGD


class LinearRegressionGD:
    def __init__(self, learning_rate=0.001, epochs=1000, method='sgd'):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.optimizer = self._create_optimizer(method)
        self.weights = None
        self.bias = None

    def _create_optimizer(self, method):
        # Фабрика для создания оптимизатора.
        optimizers = {
            'sgd': SGD(self.learning_rate),
            'nesterov': Nesterov(self.learning_rate),
            'rmsprop': RMSProp(self.learning_rate),
            'adam': Adam(self.learning_rate)
        }
        if method.lower() not in optimizers:
            raise ValueError(f"Invalid method: {method}")
        return optimizers[method.lower()]

    def _initialize_weights(self, n_features):
        self.weights = np.zeros(n_features)
        self.bias = 0

    def fit(self, x, y):
        x = np.c_[np.ones(x.shape[0]), x]  # Add bias term
        self._initialize_weights(x.shape[1])

        for _ in range(1, self.epochs + 1):
            prediction = np.dot(x, self.weights) + self.bias
            error = prediction - y
            grad_w = np.dot(x.T, error) / x.shape[0]
            grad_b = np.sum(error) / x.shape[0]

            # Обновление весов и смещения
            self.weights, self.bias = self.optimizer.update(self.weights, self.bias, grad_w, grad_b)

    def predict(self, x):
        x = np.c_[np.ones(x.shape[0]), x]
        return np.dot(x, self.weights) + self.bias
