import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from PIL import Image, ImageTk

from LinearRegressionGD import LinearRegressionGD


class LinearRegressionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linear Regression with Gradient Descent")
        self.geometry("800x700")
        self.configure(bg="#f4f4f9")
        self.style = ttk.Style(self)
        self.configure_style()
        self.create_widgets()

    def configure_style(self):
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Arial", 12), background="#f4f4f9", foreground="#333333")
        self.style.configure("TButton", font=("Arial", 12), padding=5, background="#0078d7", foreground="#ffffff")
        self.style.map("TButton", background=[("active", "#005bb5")])
        self.style.configure("TEntry", font=("Arial", 12), padding=5)
        self.style.configure("TCombobox", font=("Arial", 12), padding=5)

    def create_widgets(self):
        # Title
        self.lbl_title = ttk.Label(self, text="Linear Regression with Gradient Descent", font=("Arial", 16, "bold"))
        self.lbl_title.pack(pady=10)

        # Gradient Descent Method
        self.method_label = ttk.Label(self, text="Choose Gradient Descent Method:")
        self.method_label.pack(pady=5)
        self.method_var = tk.StringVar()
        self.method_combobox = ttk.Combobox(self, textvariable=self.method_var, state="readonly")
        self.method_combobox['values'] = ('sgd', 'nesterov', 'rmsprop', 'adam')
        self.method_combobox.current(0)  # Set default method
        self.method_combobox.pack(pady=5)

        # Learning Rate
        self.lr_label = ttk.Label(self, text="Learning Rate:")
        self.lr_label.pack(pady=5)
        self.lr_var = tk.StringVar(value="0.01")
        self.lr_entry = ttk.Entry(self, textvariable=self.lr_var, width=15)
        self.lr_entry.pack(pady=5)

        # Epochs
        self.epochs_label = ttk.Label(self, text="Number of Epochs:")
        self.epochs_label.pack(pady=5)
        self.epochs_var = tk.StringVar(value="1000")
        self.epochs_entry = ttk.Entry(self, textvariable=self.epochs_var, width=15)
        self.epochs_entry.pack(pady=5)

        # Generate Button
        self.btn_generate = ttk.Button(self, text="Generate Data and Fit Model", command=self.generate_data)
        self.btn_generate.pack(pady=10)

        # Plot Canvas
        self.canvas = tk.Canvas(self, width=700, height=400, bg="#ffffff", bd=0, highlightthickness=1, highlightbackground="#cccccc")
        self.canvas.pack(pady=20)

    def generate_data(self):
        try:
            # Validate input
            learning_rate = float(self.lr_var.get())
            epochs = int(self.epochs_var.get())
            if learning_rate <= 0 or epochs <= 0:
                raise ValueError("Learning rate and epochs must be positive.")

            # Generate data
            X, y = make_regression(n_samples=100, n_features=1, noise=15)
            X = np.c_[np.ones(X.shape[0]), X]  # Add column of ones for bias term

            # Get selected method
            selected_method = self.method_var.get()

            # Fit linear regression model
            model = LinearRegressionGD(learning_rate=learning_rate, epochs=epochs, method=selected_method)
            model.fit(X, y)
            predictions = model.predict(X)

            # Plot data and regression line
            plt.clf()
            plt.figure(figsize=(8, 6))
            plt.scatter(X[:, 1], y, color='blue', label='Data')
            plt.plot(X[:, 1], predictions, color='red', label='Regression Line')
            plt.title(f'Linear Regression with {selected_method.upper()}')
            plt.xlabel('X')
            plt.ylabel('y')
            plt.legend()

            # Save plot to display in Tkinter
            plt.savefig('plot.png')
            plt.close()  # Close the figure to free up memory

            # Display plot in Tkinter
            self.display_plot()

        except ValueError as e:
            tk.messagebox.showerror("Invalid Input", str(e))

    def display_plot(self):
        img = Image.open('plot.png')
        img = img.resize((700, 400))
        self.img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)


# Run the application
if __name__ == "__main__":
    app = LinearRegressionApp()
    app.mainloop()
