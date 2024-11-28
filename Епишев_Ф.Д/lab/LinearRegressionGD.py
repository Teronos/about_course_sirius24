import numpy as np

class LinearRegressionGD:
    def __init__(self, learning_rate=0.001, epochs=1000, method='sgd'):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.method = method
        self.weights = None
        self.bias = None
        self.EPSILON = 1e-8

    def _initialize_weights(self, n_features):
        self.weights = np.zeros(n_features)
        self.bias = 0

    def fit(self, x, y):
        x = np.c_[np.ones(x.shape[0]), x]
        self._initialize_weights(x.shape[1])

        if self.method == 'sgd':
            self._sgd(x, y)
        elif self.method == 'nesterov':
            self._nesterov(x, y)
        elif self.method == 'rmsprop':
            self._rmsprop(x, y)
        elif self.method == 'adam':
            self._adam(x, y)
        else:
            raise ValueError("Invalid method")

    def _nesterov(self, x, y):
        v_weights = np.zeros_like(self.weights)
        v_bias = 0
        gamma = 0.9
        for _ in range(self.epochs):
            # Предварительный шаг
            look_ahead_weights = self.weights - gamma * v_weights
            look_ahead_bias = self.bias - gamma * v_bias

            # Вычисление градиентов на основании предварительного шага
            prediction = np.dot(x, look_ahead_weights) + look_ahead_bias
            error = prediction - y
            grad_w = np.dot(x.T, error) / x.shape[0]
            grad_b = np.sum(error) / x.shape[0]

            # Обновление моментов
            v_weights = gamma * v_weights + self.learning_rate * grad_w
            v_bias = gamma * v_bias + self.learning_rate * grad_b

            # Обновление весов и смещения
            self.weights -= v_weights
            self.bias -= v_bias

    def _sgd(self, x, y):
        for _ in range(self.epochs):
            for i in range(x.shape[0]):
                prediction = np.dot(x[i], self.weights) + self.bias
                error = prediction - y[i]
                self.weights -= self.learning_rate * error * x[i]
                self.bias -= self.learning_rate * error

    def _rmsprop(self, x, y):
        beta = 0.9
        weights = np.zeros_like(self.weights)
        bias = 0
        for _ in range(self.epochs):
            prediction = np.dot(x, self.weights) + self.bias
            error = prediction - y
            grad_w = np.dot(x.T, error) / x.shape[0]
            grad_b = np.sum(error) / x.shape[0]

            weights = beta * weights + (1 - beta) * grad_w ** 2
            bias = beta * bias + (1 - beta) * grad_b ** 2

            self.weights -= self.learning_rate * grad_w / (np.sqrt(weights) + self.EPSILON)
            self.bias -= self.learning_rate * grad_b / (np.sqrt(bias) + self.EPSILON)

    def _adam(self, x, y):
        beta1 = 0.9
        beta2 = 0.999
        m_w = np.zeros_like(self.weights)
        v_w = np.zeros_like(self.weights)
        m_b = 0
        v_b = 0
        for t in range(1, self.epochs + 1):
            prediction = np.dot(x, self.weights) + self.bias
            error = prediction - y
            grad_w = np.dot(x.T, error) / x.shape[0]
            grad_b = np.sum(error) / x.shape[0]

            m_w = beta1 * m_w + (1 - beta1) * grad_w
            v_w = beta2 * v_w + (1 - beta2) * (grad_w ** 2)

            m_w_hat = m_w / (1 - beta1 ** t)
            v_w_hat = v_w / (1 - beta2 ** t)

            m_b = beta1 * m_b + (1 - beta1) * grad_b
            v_b = beta2 * v_b + (1 - beta2) * (grad_b ** 2)

            m_b_hat = m_b / (1 - beta1 ** t)
            v_b_hat = v_b / (1 - beta2 ** t)

            self.weights -= self.learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.EPSILON)
            self.bias -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.EPSILON)

    def predict(self, x):
        x = np.c_[np.ones(x.shape[0]), x]
        return np.dot(x, self.weights) + self.bias
