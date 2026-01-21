
class Product:
    """Класс для создания наименований продуктов и их параметров"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            """сумма произведений цены на количество у обоих объектов"""
            total_sum = self.price*self.quantity + other.price*other.quantity
            return total_sum



    @classmethod
    def new_product(cls,product_parameters: dict):
        name = product_parameters["name"]
        description = product_parameters["description"]
        price = product_parameters["price"]
        quantity = product_parameters["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Возвращает цену товара"""
        return f"{self.__price}"

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            print("Цена должна быть числом")
            return
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Проверка на понижение цены
        if self.__price is not None and price < self.__price:
            response = input(f"Вы снижаете цену с {self.__price} до {price}. Подтвердите (y/n): ").lower()
            if response != 'y':
                print("Изменение цены отменено.")
                return  # отменяет изменение

        self.__price = float(price)

    def __repr__(self):
        return self.__str__()
