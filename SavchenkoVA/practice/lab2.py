import numpy as np
import pandas as pd
from scipy.spatial import KDTree

"""
Лабораторная 2:
Пространственная интерполяция данных на основе KD-дерева. С использованием IDW и TIN методов
* Реализовать структуру KD-дерево размерности два.
* Реализовать интерполяцию данных методом idw или TIN на плоскости.
* Совместить метод интерполяции с KD-деревом для интерполяции по k ближайшим соседям,
где k - параметр функции интерполяции.
* Реализовать обёртку для функционала, которая считывает из файла опорные точки (x, y, значение),
выходные точки, в которых нужно получить интерполированные данные (x, y)
и проводила интерполяцию во всех выходных точках.
* Можно использовать сторонние библиотеки только для презентации результатов на защите лабораторной работы.
"""


class KDTreeInterpolator:
    points: np.array
    tree: KDTree

    def __init__(self, points: np.array) -> None:
        self.points = points
        self.tree = KDTree(points[:, :2])  # Создание KD-дерева по координатам (x, y)

    def idw(self, query_points: np.array, k: int = 3):
        distances, indices = self.tree.query(query_points, k=k)
        weights = 1 / (distances + 1e-10)  # Избегаем деления на ноль
        weighted_values = weights * self.points[indices, 2]  # Значения в опорных точках
        interpolated_values = weighted_values.sum(axis=1) / weights.sum(axis=1)
        return interpolated_values

def read_points_from_file(filename: str) -> np.array:
    data = pd.read_csv(filename)
    return data.values  # Возвращаем массив numpy

def lab2():
    # Чтение опорных точек из файла
    interpolator = KDTreeInterpolator(read_points_from_file('points.csv'))

    # Определение выходных точек для интерполяции
    query_points = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 1.0]])  # Пример выходных точек

    # Интерполяция значений
    interpolated_values = interpolator.idw(query_points, k=3)
    print("Интерполированные значения:", interpolated_values)

if __name__ == "__main__":
    lab2()
