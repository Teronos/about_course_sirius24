import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def image_to_np(image_path: str) -> np.ndarray:
    """Конвертирует изображение в numpy массив."""
    image = Image.open(image_path)
    image_data = np.asarray(image)
    return image_data


def apply_pca_to_channel(channel: np.ndarray, num_components: int) -> np.ndarray:
    """Применяет PCA к одному каналу изображения."""
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


def compress_image_pca(image_path: str, num_components) -> Image:
    """Применяет PCA к каждому цветовому каналу изображения."""
    image_data = image_to_np(image_path)

    # Разделяем изображение на цветовые каналы (R, G, B)
    red_channel = image_data[:, :, 0]
    green_channel = image_data[:, :, 1]
    blue_channel = image_data[:, :, 2]

    # Применяем PCA к каждому каналу
    compressed_red = apply_pca_to_channel(red_channel, num_components[0])
    compressed_green = apply_pca_to_channel(green_channel, num_components[1])
    compressed_blue = apply_pca_to_channel(blue_channel, num_components[2])

    # Объединяем обратно сжатые каналы
    compressed_image_data = np.stack((compressed_red, compressed_green, compressed_blue), axis=2)

    return Image.fromarray(compressed_image_data)


def display_images(original_image_path: str, compressed_image: Image):
    """Отображает исходное и сжатое изображение рядом друг с другом."""
    original_image = Image.open(original_image_path)

    # Настройка отображения двух изображений рядом
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(original_image)
    axes[0].set_title('Оригинальное изображение')
    axes[0].axis('off')

    axes[1].imshow(compressed_image)
    axes[1].set_title('Сжатое изображение (PCA)')
    axes[1].axis('off')

    plt.show()