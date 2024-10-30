import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def image_to_np(image_path: str) -> np.ndarray:
    image = Image.open(image_path)
    image_data = np.asarray(image)
    return image_data


def apply_pca_to_channel(channel: np.ndarray, num_components: int) -> np.ndarray:
    # Применяет МГК к одному каналу изображения.
    # Преобразуем канал в двумерный массив
    height, width = channel.shape

    # Центрируем данные
    mean = np.mean(channel, axis=0)
    centered_data = channel - mean

    # Вычисляем матрицу ковариации
    covariance_matrix = np.cov(centered_data, rowvar=False)

    # Находим собственные значения и собственные векторы
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # Сортируем собственные векторы по убыванию собственных значений
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Выбираем num_components собственных векторов
    components = sorted_eigenvectors[:, :num_components]

    # Проецируем данные на новые компоненты
    compressed_data = np.dot(centered_data, components)

    # Восстанавливаем данные
    reconstructed_data = np.dot(compressed_data, components.T) + mean
    reconstructed_data = np.clip(reconstructed_data, 0, 255).astype(np.uint8)

    return reconstructed_data

from concurrent.futures import ThreadPoolExecutor

def compress_image_pca(image_path: str, compress_factor: list) -> Image:#
    image_data = image_to_np(image_path)
    # Разделяем изображение на цветовые каналы (R, G, B)
    red_channel = image_data[:, :, 0]
    green_channel = image_data[:, :, 1]
    blue_channel = image_data[:, :, 2]

    # Определяем функцию для многопоточной обработки
    def pca_compression(channel, components):
        return apply_pca_to_channel(channel, components)

    # Используем ThreadPoolExecutor для параллельного сжатия
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_red = executor.submit(pca_compression, red_channel, compress_factor[0])
        future_green = executor.submit(pca_compression, green_channel, compress_factor[1])
        future_blue = executor.submit(pca_compression, blue_channel, compress_factor[2])

        # Получаем результаты выполнения функций
        compressed_red = future_red.result()
        compressed_green = future_green.result()
        compressed_blue = future_blue.result()

    # Объединяем обратно сжатые каналы
    compressed_image_data = np.stack((compressed_red, compressed_green, compressed_blue), axis=2)

    return Image.fromarray(compressed_image_data)
