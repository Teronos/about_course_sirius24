from Optimizer import Optimizer


class SGD(Optimizer):
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def update(self, weights, bias, grad_w, grad_b):
        weights -= self.learning_rate * grad_w
        bias -= self.learning_rate * grad_b
        return weights, bias