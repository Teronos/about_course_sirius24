from abc import ABC, abstractmethod
import numpy as np

class Optimizer(ABC):
    """Абстрактный базовый класс для оптимизаторов."""

    @abstractmethod
    def update(self, weights, bias, grad_w, grad_b):
        pass