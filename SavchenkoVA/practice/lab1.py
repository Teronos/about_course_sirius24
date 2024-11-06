import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

"""
Лабораторная 1:
Собственная реализация семейства методов градиентного спуска(SGD/NESTEROV/RMSProp/ADAM).
* Выбрать три набора данных для линейной регрессии.
* Реализовать n-мерные варианты алгоритмов и использовать их для линейной регрессии.
* Реализовать обёртку для функционала, которая принимает на вход набор данных в нужном формате
и формирует вектор весов со смещением модели, а также визуализирует результаты работы.
* Можно использовать сторонние библиотеки только для презентации результатов на защите лабораторной работы.
"""


class LinearRegression:
    method: str
    learning_rate: float
    n_iterations: int
    momentum: float
    beta1: float
    beta2: float
    epsilon: float
    weights: np.array
    bias: int

    def __init__(self, method: str = 'SGD', learning_rate: float = 0.01, n_iterations: int = 1000,
                 momentum: float = 0.9, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-8) -> None:
        self.method = method
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.momentum = momentum
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

    def fit(self, X: np.array, y: np.array) -> None:
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        m = np.zeros(n_features)
        v = np.zeros(n_features)
        v_bias = 0

        for i in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            error = y_predicted - y

            if self.method == 'SGD':
                dw = (1 / n_samples) * np.dot(X.T, error)
                db = (1 / n_samples) * np.sum(error)
                self.weights -= self.learning_rate * dw
                self.bias -= self.learning_rate * db

            elif self.method == 'Nesterov':
                db = (1 / n_samples) * np.sum(error)
                m_prev = m.copy()
                m = self.momentum * m - self.learning_rate * (1 / n_samples) * np.dot(X.T, error)
                self.weights += -self.momentum * m_prev + (1 + self.momentum) * m
                self.bias -= self.learning_rate * db

            elif self.method == 'RMSProp':
                dw = (1 / n_samples) * np.dot(X.T, error)
                m = self.beta2 * m + (1 - self.beta2) * dw ** 2
                self.weights -= self.learning_rate * dw / (np.sqrt(m) + self.epsilon)

            elif self.method == 'Adam':
                db = (1 / n_samples) * np.sum(error)
                dw = (1 / n_samples) * np.dot(X.T, error)
                v = self.beta1 * v + (1 - self.beta1) * dw
                m = self.beta2 * m + (1 - self.beta2) * (dw ** 2)
                v_bias = self.beta1 * v_bias + (1 - self.beta1) * db
                m_hat = v / (1 - self.beta1 ** (i + 1))
                v_hat = m / (1 - self.beta2 ** (i + 1))
                self.weights -= self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)
                self.bias -= self.learning_rate * v_bias / (np.sqrt(v_hat) + self.epsilon)

    def predict(self, X: np.array) -> np.dot:
        return np.dot(X, self.weights) + self.bias


def visualize_results(X: np.array, y: np.array, model: LinearRegression) -> None:
    plt.scatter(X, y, color='blue', label='Данные')
    y_pred = model.predict(X)
    plt.plot(X, y_pred, color='red', label='Предсказание')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Линейная регрессия')
    plt.legend()
    plt.savefig('result_lab1.jpg')
    plt.show()


def lab3() -> None:
    # Генерация данных
    X, y = make_regression(n_samples=100, n_features=1, noise=10)
    X = X.reshape(-1, 1)

    # Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучение модели
    model = LinearRegression(method='Adam', learning_rate=0.01, n_iterations=1000)
    model.fit(X_train, y_train)

    # Визуализация результатов
    visualize_results(X_test, y_test, model)


if __name__ == "__main__":
    lab3()
