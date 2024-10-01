
class Notebook:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

        self.laptop_name = f"{self.brand} {self.model}"



    def full_name(self):
        return str(f"{self.first_name} {self.last_name}")
    

    def get_laptop_name(self):
        return self.laptop_name



hp = Notebook('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.get_laptop_name()) # выводит "hp 15-bw0xx"
print(hp.laptop_name)
