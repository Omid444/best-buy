class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price must be non-negative")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        return self.quantity


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price:{self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:

        if quantity > self.quantity:
            raise ValueError("Quantity is more than quantity of available items")
        if quantity <= 0:
            raise ValueError("Quantity cannot be zero or negative")
        if isinstance(quantity, str):
            raise ValueError("Quantity cannot be a string")
        if not quantity:
            raise ValueError("Quantity cannot be empty")

        self.quantity -= quantity
        return round(float(self.price * quantity), 2)

