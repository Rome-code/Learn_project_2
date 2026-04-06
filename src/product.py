
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
        if type(self) == type(other):
            """сумма произведений цены на количество у обоих объектов"""
            total_sum = self.price*self.quantity + other.price*other.quantity
            return total_sum
        else:
            raise TypeError


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
        return self.__price

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


class Smartphone(Product):
    """Класс категории товаров «Смартфон»"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency #производительность
        self.model = model
        self.memory = memory    #объем встроенной памяти
        self.color = color

    def __add__(self, other):

        if type(self) == type(other):
            return self.price + other.price
        else:
            raise TypeError


class Os(Smartphone):
    """Подкласс категории Smartphone, отражающий деление по операционным системам"""
    def __init__(self, name, description, price, quantity,operation_system, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity, efficiency, model, memory, color)
        self.operation_system = operation_system
        self.efficiency = efficiency  # производительность
        self.model = model
        self.memory = memory  # объем встроенной памяти
        self.color = color


class ConnectionSpeed(Smartphone):
    """Подкласс категории Smartphone, отражающий деление по скорости подключения к интернету"""
    def __init__(self, name, description, price, quantity, connection_speed, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity, efficiency, model, memory, color)
        self.connection_speed = connection_speed
        self.efficiency = efficiency   #производительность
        self.model = model
        self.memory = memory    #объем встроенной памяти
        self.color = color


class LawnGrass(Product):
    """Класс категории товаров «Трава газонная» """
    def __init__(self,name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.germination_period = germination_period    #срок прорастания
        self.color = color

    def __add__(self, other):

        if type(self) == type(other):
            return self.price + other.price
        else:
            raise TypeError


class GrowthHeight(LawnGrass):
    """Подкласс категории товаров «Трава газонная», отражающий деление по высоте роста """
    def __init__(self,name, description, price, quantity, country, germination_period, color, growth_height):
        super().__init__(name, description, price, quantity, country, germination_period, color)
        self.country = country      # страна-производитель
        self.germination_period = germination_period    #срок прорастания
        self.color = color
        self.growth_height = growth_height


class Resistance(LawnGrass):
    """Подкласс категории товаров «Трава газонная», отражающий деление
    по зимостойкоси и засухоустойчивости, способности переносить частые стрижки. """
    def __init__(self,name, description, price, quantity, country, germination_period, color, resistance):
        super().__init__(name, description, price, quantity,country, germination_period, color)
        self.country = country  # страна-производитель
        self.germination_period = germination_period    #срок прорастания
        self.color = color
        self.resistance = resistance

