import numpy as np
from PIL import Image

"""
Лабораторная 3:
Сжатие изображения с потерей качества на основе МГК.
"""

"""
Функция открытия изображения и преобразования в массив
Принимает путь к изображению
Возвращает массив
"""


def image_to_np(image_path: str) -> np.array:
    return np.array(Image.open(image_path))


"""
Функция сжатия изображения
Принимает путь к изображению
Возвращает сжатое изображение
"""


def compress_image(image_path: str, num_components: int = 50) -> Image:
    image_data = image_to_np(image_path)

    # Преобразуем изображение в двумерный массив
    reshaped_image = image_data.reshape(-1, 3)

    # Центрируем данные
    mean = np.mean(reshaped_image, axis=0)
    centered_data = reshaped_image - mean

    # Вычисляем матрицу ковариации
    covariance_matrix = np.cov(centered_data, rowvar=False)

    # Находим собственные значения и собственные векторы
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # Сортируем собственные векторы по убыванию собственных значений
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Выбираем первые num_components собственных векторов
    components = sorted_eigenvectors[:, :num_components]

    # Проецируем данные на новые компоненты
    compressed_data = np.dot(centered_data, components)

    # Восстанавливаем изображение
    reconstructed_data = np.dot(compressed_data, components.T) + mean
    reconstructed_data = np.clip(reconstructed_data, 0, 255).astype(np.uint8)

    # Преобразуем обратно в оригинальный формат изображения
    compressed_image = Image.fromarray(reconstructed_data.reshape(image_data.shape))
    return compressed_image


if __name__ == "__main__":
    compressed_img = compress_image('1.jpg')
    compressed_img.save('result_lab3.jpg')
    compressed_img.show()
