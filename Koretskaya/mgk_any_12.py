import numpy as np
import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, Label, Scale, Button
from PIL.Image import SupportsArrayInterface


class ImageCompressor:

    __original_image: np.ndarray | None = None  # Приватное поле оригинального изображения
    __compressed_image: np.ndarray | None = None  # Приватное поле сжатого изображения

    def __init__(self) -> None:

        pass

    def load_image(self, file_path: str) -> np.ndarray | None:
        """
        Загружает изображение и конвертирует его в RGB.

        Args:
            file_path (str): Путь к изображению.

        Returns:
            np.ndarray | None: Загруженное изображение.
        """
        self.__original_image = cv2.imread(file_path)
        if self.__original_image is not None:
            self.__original_image = cv2.cvtColor(self.__original_image, cv2.COLOR_BGR2RGB)
        return self.__original_image

    def compress_image(self, compression_percentage: int) -> np.ndarray | None:
        """
        Сжимает изображение с использованием SVD.

        Args:
            compression_percentage (int): Процент сжатия.

        Returns:
            np.ndarray | None: Сжатое изображение.
        """
        if self.__original_image is None:
            return None

        R, G, B = self.__original_image[:, :, 0], self.__original_image[:, :, 1], self.__original_image[:, :, 2]

        # Применяем SVD
        U_R, S_R, Vt_R = np.linalg.svd(R, full_matrices=False)
        U_G, S_G, Vt_G = np.linalg.svd(G, full_matrices=False)
        U_B, S_B, Vt_B = np.linalg.svd(B, full_matrices=False)

        total_singular_values: int = min(R.shape[0], R.shape[1])
        k: int = int(total_singular_values * (1 - compression_percentage / 100))

        # Восстанавливаем сжатое изображение
        R_compressed = np.dot(U_R[:, :k], np.dot(np.diag(S_R[:k]), Vt_R[:k, :]))
        G_compressed = np.dot(U_G[:, :k], np.dot(np.diag(S_G[:k]), Vt_G[:k, :]))
        B_compressed = np.dot(U_B[:, :k], np.dot(np.diag(S_B[:k]), Vt_B[:k, :]))

        self.__compressed_image = np.stack((R_compressed, G_compressed, B_compressed), axis=-1)
        self.__compressed_image = np.clip(self.__compressed_image, 0, 255).astype(np.uint8)

        return self.__compressed_image

    def get_original_image(self) -> np.ndarray | None:
        """Возвращает оригинальное изображение."""
        return self.__original_image

    def get_compressed_image(self) -> np.ndarray | None:
        """Возвращает сжатое изображение."""
        return self.__compressed_image


class ImageCompressorApp:
    """
    Класс для создания графического интерфейса сжатия изображений.
    """

    __compressor: ImageCompressor
    master: tk.Tk
    def __init__(self, master: tk.Tk) -> None:
        """
        Инициализация интерфейса приложения.

        Args:
            master (tk.Tk): Главное окно Tkinter.
        """
        self.master: tk.Tk = master
        self.master.title("Image Compression App")
        self.__compressor = ImageCompressor()

        # Элементы управления интерфейса
        self.__load_button: Button = Button(master, text="Load Image", command=self.__load_image)
        self.__load_button.pack()

        self.__compression_scale: Scale = Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, label="Compression %")
        self.__compression_scale.set(50)
        self.__compression_scale.pack()

        self.__compress_button: Button = Button(master, text="Compress", command=self.__compress_image)
        self.__compress_button.pack()

        self.__original_label: Label = Label(master, width=500, height=500)
        self.__original_label.pack(side=tk.LEFT)

        self.__compressed_label: Label = Label(master, width=500, height=500)
        self.__compressed_label.pack(side=tk.RIGHT)

    def __load_image(self) -> None:
        """Загружает изображение с помощью диалога выбора файла."""
        file_path: str = filedialog.askopenfilename()
        if file_path:
            image: np.ndarray | None = self.__compressor.load_image(file_path)
            if image is not None:
                self.__display_image(image, self.__original_label)

    def __compress_image(self) -> None:
        """Сжимает изображение и отображает результат."""
        compression_percentage: int = self.__compression_scale.get()
        compressed_image: np.ndarray | None = self.__compressor.compress_image(compression_percentage)
        if compressed_image is not None:
            self.__display_image(compressed_image, self.__compressed_label)

    def __display_image(self, image: SupportsArrayInterface, label: Label) -> None:
        """
        Отображает изображение в указанной метке.

        Args:
            image (SupportsArrayInterface): Изображение.
            label (Label): Tkinter Label для отображения.
        """
        image_pil: Image.Image = Image.fromarray(image)
        image_pil.thumbnail((540, 540))
        image_tk: ImageTk.PhotoImage = ImageTk.PhotoImage(image_pil)
        label.config(image=image_tk)
        label.image = image_tk


if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    root.geometry('1050x550+600+600')
    root.resizable(True, True)
    app: ImageCompressorApp = ImageCompressorApp(root)
    root.mainloop()
