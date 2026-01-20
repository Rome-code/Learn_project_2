from itertools import product

class Category:
    """Класс для создания категорий продукции"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1

        Category.product_count += len(products)

    def __str__(self):
        products_quantity_sum = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {products_quantity_sum} шт."
