class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def laptop_name(self):
        return f"{self.brand} {self.model}"
hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)  # Выведет 57000
print(hp.laptop_name())  # Выведет "hp 15-bw0xx"