class Product:
    """Класс для создания наименований продуктов и их параметров"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            """сумма произведений цены на количество у обоих объектов"""
            total_sum = self.price*self.quantity + other.price*other.quantity
            return total_sum





