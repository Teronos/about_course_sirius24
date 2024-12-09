import numpy as np
import cv2  # OpenCV для обработки изображений
from PIL import Image, ImageTk  # Tkinter
import tkinter as tk  # ГИ
from tkinter import filedialog, Label, Scale, Button
import os  # Работа с файлами

class ImageCompressor:
    def __init__(self):
        self.original_image = None  # Инициализируем переменную для оригинального изображения
        self.compressed_image = None  # Инициализируем переменную для сжатого изображения

    def load_image(self, file_path):
        self.original_image = cv2.imread(file_path)  # Загружаем изображение с помощью OpenCV
        # Преобразуем изображение из BGR в RGB
        self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        return self.original_image

    def compress_image(self, compression_percentage):
        if self.original_image is None:  # Проверяем, загружено ли оригинальное изображение
            return None

        # Разделение изображения на цветовые каналы
        R, G, B = self.original_image[:, :, 0], self.original_image[:, :, 1], self.original_image[:, :, 2]

        # Применяем сингулярное разложение (SVD) для каждого канала
        U_R, S_R, Vt_R = np.linalg.svd(R, full_matrices=False)
        U_G, S_G, Vt_G = np.linalg.svd(G, full_matrices=False)
        U_B, S_B, Vt_B = np.linalg.svd(B, full_matrices=False)

        total_singular_values = min(R.shape[0], R.shape[1])  # Определяем общее количество сингулярных значений
        k = int(total_singular_values * (1 - compression_percentage / 100))  # Вычисляем количество значений для сжатия

        # Сжимаем каждый цветовой канал
        R_compressed = np.dot(U_R[:, :k], np.dot(np.diag(S_R[:k]), Vt_R[:k, :]))
        G_compressed = np.dot(U_G[:, :k], np.dot(np.diag(S_G[:k]), Vt_G[:k, :]))
        B_compressed = np.dot(U_B[:, :k], np.dot(np.diag(S_B[:k]), Vt_B[:k, :]))

        # Объединяем сжатые каналы обратно в одно изображение
        self.compressed_image = np.stack((R_compressed, G_compressed, B_compressed), axis=-1)
        self.compressed_image = np.clip(self.compressed_image, 0, 255).astype(np.uint8)  # Ограничиваем значения пикселей

        return self.compressed_image

class ImageCompressorApp:
    def __init__(self, master):  # Метод инициализации окна
        self.master = master  # Сохраняем ссылку на главное окно
        self.master.title("Сжатие МГК")

        self.compressor = ImageCompressor()  # Создаем экземпляр класса ImageCompressor

        # Создаем кнопку для загрузки изображения
        self.load_button = Button(master, text="Загрузить", command=self.load_image)
        self.load_button.pack()

        # Создаем ползунок для выбора процента сжатия
        self.compression_scale = Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, label="Compression %")
        self.compression_scale.set(50)  # Устанавливаем начальное значение в 50%
        self.compression_scale.pack()

        # Создаем кнопку для сжатия изображения
        self.compress_button = Button(master, text="Сжать", command=self.compress_image)
        self.compress_button.pack()

        # Создаем метки для отображения изображений
        self.original_label = Label(master)  # Метка для оригинального изображения
        self.original_label.pack(side=tk.LEFT)
        self.compressed_label = Label(master)  # Метка для сжатого изображения
        self.compressed_label.pack(side=tk.RIGHT)

        # Метки для отображения размеров изображений
        self.original_size_label = Label(master, text="Original Size: 0 KB")
        self.original_size_label.pack()
        self.compressed_size_label = Label(master, text="Compressed Size: 0 KB")
        self.compressed_size_label.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()  # Открываем диалоговое окно для выбора файла
        if file_path:
            original_image = self.compressor.load_image(file_path)  # Загружаем изображение
            self.display_image(original_image, self.original_label)  # Отображаем оригинальное изображение

            # Обновление размера оригинального изображения
            original_size_kb = os.path.getsize(file_path) / 1024  # Получаем размер файла в килобайтах
            self.original_size_label.config(text=f"Original Size: {original_size_kb:.2f} KB")  # Обновляем текст метки

    def compress_image(self):
        compression_percentage = self.compression_scale.get()  # Получаем процент сжатия из ползунка
        compressed_image = self.compressor.compress_image(compression_percentage)  # Сжимаем изображение
        if compressed_image is not None:
            # Сохраняем сжатое изображение
            compressed_image_pil = Image.fromarray(compressed_image)  # Преобразуем массив в формат PIL
            compressed_image_pil.save('compressed_image.jpg', dpi=(72, 72))  # Сохраняем изображение в файл

            # Обновляем размер сжатого изображения
            compressed_size_kb = os.path.getsize('compressed_image.jpg') / 1024  # Получаем размер сжатого изображения
            self.compressed_size_label.config(text=f"Compressed Size: {compressed_size_kb:.2f} KB")

            # Отображаем сжатое изображение
            self.display_image(compressed_image, self.compressed_label)

    def display_image(self, image, label):  # Метод для отображения изображения
        image_pil = Image.fromarray(image)  # Преобразуем массив в объект PIL
        image_tk = ImageTk.PhotoImage(image_pil)  # Преобразуем объект PIL в формат, совместимый с Tkinter
        label.config(image=image_tk)  # Устанавливаем изображение в метке
        label.image = image_tk  # Сохраняем ссылку на изображение, чтобы избежать его уничтожения

if __name__ == "__main__":
    root = tk.Tk()  # Создаем главное окно Tkinter
    app = ImageCompressorApp(root)  # Инициализируем приложение
    root.mainloop()  # Запускаем главный цикл обработки событий
