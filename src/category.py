from src.product import Product

class Category:
    """Класс для создания категорий продукции"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1

    @property
    def products(self):
        """Свойство возвращающее список"""
        return self.__products

    def add_product(self, product):
        """Добавляет новые товары"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

        else:
            raise TypeError("Можно добавлять только объекты класса Product.")

    def get_products(self):
        result = []
        for product in self.__products:
            result.append(f"Название продукта: {product.name}, {product.price} руб., Остаток: {product.quantity}")
        return result
